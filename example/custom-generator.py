from fable import Table, Field
from fable.models import TableConfig, FieldConfig
from fable.generators import AbstractBaseGenerator

from typing import List
import logging

logging.basicConfig(level=logging.WARNING)


# Custom generator
class CustomGen(AbstractBaseGenerator):
    required_params = None

    @classmethod
    def generate(cls, row_count: int) -> List[int]:
        values = []
        for _ in range(row_count):
            values.append(cls._generate_value())

        return values

    @classmethod
    def _generate_value(cls):
        return 2

    @classmethod
    def _validate_params(cls):
        pass


# Define a TableConfig
example_table_config = TableConfig(name="example_table", row_count=1000)

# Instantiate a table using our TableConfig
example_table = Table(example_table_config)

# Define some FieldConfigs, each with custom params
example_field_config = FieldConfig(
    name="example_field_1",
    dtype=int,
    generator=CustomGen,
)

field = Field(example_field_config)

example_table.add_field(field)

example_table.populate()

print(example_table.head())
