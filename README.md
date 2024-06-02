### Concepts

*Generators*: Generators are the mechanism by which a Field actually gets populated with data.
There are different types of generators (see [generators.py](src/fable/generators.py)). Each
generator is a class and has a method to validate parameters passed to the generator, a method
to generate a single value, and then a method that gets called in
[core.py](src/fable/core.py) which combines the other two methods, the parameters, and the
associated Table's `row_count` to generate all the requested values.

*Field*: A `Field` represents a single column in a Table. A `Field` is instantiated based on a
`FieldConfig` found in [models.py](src/fable/models.py), which includes a `name`, and
`params` which will be passed to the generator associated with that `Field`.

*Table*: A `Table` is a collection of Fields. Defined in [models.py](src/fable/models.py), each `Table`
is instantiated based on a `TableConfig` and includes a `name` and a `row_count`. The `row_count`
will be passed to the `populate()` method of each `Field` associated with a `Table`, and in turn to
the `generate()` method of each generator associated with each `Field`. 

A `Table` is stored in a Polars DataFrame.

### Usage
```python
from fable import Table, Field
from fable.models import TableConfig, FieldConfig
import fable.generators as fg

# Define a TableConfig
users_table_config = TableConfig(name="users", row_count=1000)

# Define some FieldConfigs
score_conf = FieldConfig(
    name="score",
    dtype=int,
    generator=fg.NumericGenerator,
    params={"lower_bound": 350, "upper_bound": 850},
)

name_conf = FieldConfig(
    name="name",
    dtype=str,
    generator=fg.StringGenerator,
)

birthday_conf = FieldConfig(
    name="birthday",
    dtype=str,
    generator=fg.DateGenerator,
)

# Instantiate a table using our TableConfig
users_table = Table(users_table_config)

# Instantiate some fields using our field config
score = Field(score_conf)
name = Field(name_conf)
birthday = Field(birthday_conf)

# Add the Fields to the Table
example_table.add_fields(field_list)

# Add some data to the Table
example_table.populate()

# Inspect the data in the Table
example_table.head()
```
