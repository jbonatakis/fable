from pydantic import BaseModel

from .types import FableType


class TableConfig(BaseModel):
    name: str
    row_count: int = 1_000


class FieldConfig(BaseModel):
    name: str
    dtype: FableType.__class__
    params: dict


class FieldMetadata(BaseModel):
    dtype: FableType.__class__
    position: int
