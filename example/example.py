from fable import Table, Field
from fable.models import TableConfig, FieldConfig
from fable.types import Integer, Varchar

import logging

logging.basicConfig(level=logging.WARNING)

# Define a TableConfig
example_table_config = TableConfig(name="example_table", row_count=1000)

# Define some FieldConfigs, each with custom params
example_field_config = FieldConfig(
    name="example_field_1",
    ftype=Integer,
    params={"lower_bound": -2500, "upper_bound": -2000},
)

example_field2_config = FieldConfig(
    name="example_field_2",
    ftype=Varchar,
    params={"lower_bound": 2500, "upper_bound": 3000},
)

example_field3_config = FieldConfig(
    name="example_field_3", ftype=Integer, params={"lower_bound": 0, "upper_bound": 10}
)

# Instantiate a table using our TableConfig
example_table = Table(example_table_config)

# Instantiate some fields using our field config
example_field = Field(example_field_config)
example_field2 = Field(example_field2_config)
example_field3 = Field(example_field3_config)

field_list = [
    example_field,
    example_field2,
    example_field3,
]

print(example_table, "\n")
for field in field_list:
    example_table.add_field(field)

for field in example_table.fields:
    print(field)


print("\n", example_table.__dict__)
example_table.remove_field("example_field_1")
print()
print(example_table.field_map)

example_table.add_field(Field(example_field_config))
print(example_table.field_map)
example_table.populate()
print(example_table.head())
print(example_table.data.count())

try:
    example_table.link(example_field, example_field2, example_field2)
except ValueError:
    print(f"Failed to link fields {example_field.name} and {example_field2.name}")

example_table.to_csv("example/out.csv", separator="|", float_precision=2)
