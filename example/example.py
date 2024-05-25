from fable import Table, Field
from fable.configs import TableConfig, FieldConfig

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
