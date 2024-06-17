from fable import Table, Field
from fable.models import TableConfig, FieldConfig
import fable.generators as fg

import logging

logging.basicConfig(level=logging.WARNING)

# Define a TableConfig
users_table_config = TableConfig(name="users", row_count=1000)

# Define some FieldConfigs, each with custom params
score_conf = FieldConfig(
    name="score",
    dtype=int,
    generator=fg.NumericGenerator,
    lower_bound=350,
    upper_bound=850,
)

name_conf = FieldConfig(
    name="name",
    dtype=str,
    generator=fg.StringGenerator,
)

birthday_conf = FieldConfig(
    name="birthday",
    dtype=str,
    # generator=fg.DateGenerator
    generator=fg.FablegenDate,
    start_date="1993-10-25",
    end_date="2024-06-17",
)

# Instantiate a table using our TableConfig
users_table = Table(users_table_config)

# Instantiate some fields using our field config
score = Field(score_conf)
name = Field(name_conf)
birthday = Field(birthday_conf)

field_list = [
    score,
    name,
    birthday,
]

print(users_table, "\n")
for field in field_list:
    users_table.add_field(field)

for field in users_table.fields:
    print(field)

users_table.remove_field("score")
users_table.add_field(Field(score_conf))
print("\n", users_table)

users_table.populate(timing=True)
print(users_table.head())
print(users_table.data.count())

users_table.to_csv("example/out.csv", separator="|", float_precision=2)
