from pydantic import BaseModel


class TableConfig(BaseModel):
    name: str
    row_count: int = 1_000


class FieldConfig(BaseModel):
    name: str
    dtype: str


class FieldMetadata(BaseModel):
    dtype: str
    position: int
