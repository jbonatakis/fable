from typing import List


class Field:
    def __init__(self, name: str, dtype: str):
        self.name = name
        self.dtype = dtype

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Table:
    def __init__(self, name: str):
        self.name = name
        self.fields: List[Field] = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def add_field(self, field: Field):
        if field not in self.fields:
            self.fields.append(field)
        else:
            raise Exception("Duplicate field")
