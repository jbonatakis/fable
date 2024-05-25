from typing import List

import random

import polars as pl
from .configs import FieldConfig, FieldMetadata, TableConfig

# TODO: Find a better place for this?
pl.Config.set_tbl_hide_dataframe_shape(True)
pl.Config.set_tbl_hide_column_data_types(True)


class Field:
    """ """

    def __init__(self, config: FieldConfig):
        self.name = config.name
        self.dtype = config.dtype

        self.values: List[self.dtype] = []

    def __str__(self):
        return f"{str(self.__class__)} : {str(self.__dict__)}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def populate(self, row_count: int):
        """Populate this field"""
        for _ in range(row_count):
            # Placeholder
            self.values.append(random.randint(0, 5_000))


class Table:
    """ """

    def __init__(self, config: TableConfig):
        self.name = config.name
        self.row_count = config.row_count

        self.field_map = {}
        self.fields: List[Field] = []
        self.data = None

    def __str__(self):
        return f"{str(self.__class__)} : {str(self.__dict__)}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def head(self, rows: int = 10):
        if self.data is None:
            raise Exception("Table has not been populated")
        return self.data.head(rows)

    def add_field(self, field: Field):
        if field.name not in self.field_map:
            self.field_map[field.name] = FieldMetadata(
                dtype=field.dtype, position=1 + len(self.fields)
            )
            self.fields.append(field)
        else:
            raise Exception(f"Duplicate field: {field.name}")

    def remove_field(self, field_name: str):
        position = self.field_map[field_name].position
        self.fields.pop(position - 1)
        del self.field_map[field_name]
        # Field map entry position needs to update when fields are removed
        for _, value in self.field_map.items():
            if value.position > position:
                value.position -= 1

    def populate(self):
        """Populate the fields associated with this table"""
        if self.data is not None:
            raise Exception("This table has already been populated")

        for field in self.fields:
            field.populate(self.row_count)

        self.data = pl.DataFrame({field.name: field.values for field in self.fields})

    def truncate(self):
        self.data = None

    def drop(self):
        self.data = None
        self.fields = []
        self.field_map = {}

    def load_to(self, target):
        """Load table to a target database"""
        pass
