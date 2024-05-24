from typing import List


class Field:
    def __init__(self, name: str, dtype: str):
        self.name = name
        self.dtype = dtype


class Table:
    def __init__(self, name: str):
        self.name = name
        self.fields: List[Field] = []

    def add_field(self, field: Field):
        self.fields.append(field)
