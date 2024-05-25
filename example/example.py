from fable import Table, Field
from fable.models import TableConfig, FieldConfig

example_table_config = TableConfig(name="example_table", row_count="500")
example_field_config = FieldConfig(name="example_field_1", dtype="varchar")
example_field2_config = FieldConfig(name="example_field_2", dtype="varchar")
example_field3_config = FieldConfig(name="example_field_3", dtype="varchar")

example_table = Table(example_table_config)

field_list = [
    Field(example_field_config),
    Field(example_field2_config),
    Field(example_field3_config),
]

example_field = Field(example_field_config)
example_field2 = Field(example_field2_config)
example_field3 = Field(example_field3_config)

print(example_table)
for field in field_list:
    example_table.add_field(field)

for field in example_table.fields:
    print(field)

print(example_table)
example_table.remove_field("example_field_1")
print()
print(example_table.field_map)

example_table.add_field(Field(example_field_config))
print(example_table.field_map)
example_table.populate()
print(example_table.head(5))
print(example_table.data.count())

try:
    example_table.link(example_field, example_field2, example_field2)
except ValueError:
    print(f"Failed to link fields {example_field.name} and {example_field2.name}")

example_table.to_csv("example/out.csv", separator="|", float_precision=2)
