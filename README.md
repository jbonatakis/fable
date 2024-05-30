### Concepts

*ftypes*: ftypes (Fable Types) define what kind of data each `Field` generates. Notices that in 
[models.py](src/fable/models.py), the `FieldConfig` class requires an `ftype`. This should map to
a defined type in [types.py](src/fable/models.py).

*Generators*: Generators are the mechanism by which a Field actually gets populated with data.
There are different types of generators (see [generators.py](src/fable/generators.py)). Each
generator is a class and has a method to validate parameters passed to the generator, a method
to generate a single value based on the associated `ftype`, and then a method that gets called in
[core.py](src/fable/core.py) which combines the other two methods, the parameters, and the
associated Table's `row_count` to generate all the requested values.

*Field*: A `Field` represents a single column in a Table. A `Field` is instantiated based on a
`FieldConfig` found in [models.py](src/fable/models.py), which includes a `name`, an `ftype`, and
`params` which will be passed to the generator associated with that Field's `ftype`.

*Table*: A `Table` is a collection of Fields. Defined in [models.py](src/fable/models.py), each `Table`
is instantiated based on a `TableConfig` and includes a `name` and a `row_count`. The `row_count`
will be passed to the `populate()` method of each `Field` associated with a `Table`, and in turn to
the `generate()` method of each generator associated with the `ftype` of each `Field`. 

A `Table` is stored in a Polars DataFrame.
