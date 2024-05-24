import fable

example_table = fable.Table("example_table")
print(example_table.name)

example_field_1 = fable.Field("example_field_1", "varchar")
example_table.add_field(example_field_1)

example_field_2 = fable.Field("example_field_2", "varchar")
example_table.add_field(example_field_2)

for field in example_table.fields:
    print(field.__dict__)
