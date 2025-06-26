from bson import ObjectId

class PyObjectId(ObjectId):
  @classmethod
  def __get_validators__(cls):
    yield cls.validate

  @classmethod
  def validate(cls, v, field): # Add 'field' as a parameter
    if not ObjectId.is_valid(v):
      raise ValueError("Invalid ObjectId")
    return ObjectId(v)