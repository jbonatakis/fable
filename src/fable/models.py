from typing import Any
from pydantic import BaseModel

from .generators import AbstractBaseGenerator


class TableConfig(BaseModel):
    name: str
    row_count: int = 1_000


class FieldConfig(BaseModel):
    name: str
    dtype: Any
    # TODO: This is bad
    generator: AbstractBaseGenerator.__class__.__class__
    params: dict[str, Any] = None


class FieldMetadata(BaseModel):
    dtype: type
    position: int
