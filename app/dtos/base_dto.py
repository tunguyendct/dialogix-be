from abc import ABC, abstractmethod
from typing import Any, Dict, TypeVar, Generic


T = TypeVar('T')

class BaseDTO(ABC, Generic[T]):
    """Base DTO class for data transfer objects"""

    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> T:
        """Convert dictionary to DTO instance."""
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convert DTO instance to dictionary"""
        pass