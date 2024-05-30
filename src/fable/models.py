from typing import Any
from pydantic import BaseModel

from .types import FableType


class TableConfig(BaseModel):
    name: str
    row_count: int = 1_000


class FieldConfig(BaseModel):
    name: str
    ftype: FableType.__class__
    params: dict[str, Any]


class FieldMetadata(BaseModel):
    ftype: FableType.__class__
    position: int
