from typing import Any
from bson import ObjectId
from pydantic_core import core_schema

class PyObjectId(str):
    """
    Custom Pydantic type for MongoDB's ObjectId.
    """
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler
    ) -> core_schema.CoreSchema:
        """
        Defines the Pydantic v2 core schema for this type.

        This schema handles:
        1.  Validation: Accepts a valid ObjectId string or an existing ObjectId instance.
        2.  Serialization: Converts ObjectId instances to strings.
        3.  JSON Schema: Represents the type as a string in the OpenAPI docs.
        """
        def validate_from_str(value: str) -> ObjectId:
            """Validate a string and convert to ObjectId."""
            if not ObjectId.is_valid(value):
                raise ValueError("Invalid ObjectId")
            return ObjectId(value)

        # Schema for when the input is a string
        from_str_schema = core_schema.chain_schema(
            [
                core_schema.str_schema(),
                core_schema.no_info_plain_validator_function(validate_from_str),
            ]
        )

        # For JSON Schema, we just want to represent it as a string.
        # The pattern is a good addition for client-side validation and documentation.
        json_schema = core_schema.str_schema(pattern=r'^[0-9a-fA-F]{24}$')

        return core_schema.json_or_python_schema(
            # For JSON, we validate from a string. This is also used for OpenAPI schema generation.
            json_schema=json_schema,
            # For Python, we can accept a string (which will be validated) or an existing ObjectId instance.
            python_schema=core_schema.union_schema([core_schema.is_instance_schema(ObjectId), from_str_schema]),
            serialization=core_schema.plain_serializer_function_ser_schema(lambda instance: str(instance)),
        )
