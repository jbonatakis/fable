import pytest

from fable import Table, Field
from fable.models import TableConfig, FieldConfig
from fable.types import Integer


def test_field_equality():
    config = FieldConfig(
        name="field", dtype=Integer, params={"lower_bound": 0, "upper_bound": 10}
    )
    field_1 = Field(config)
    field_2 = Field(config)
    field_3 = Field(
        FieldConfig(
            name="other_field",
            dtype=Integer,
            params={"lower_bound": 0, "upper_bound": 10},
        )
    )

    assert field_1 == field_2
    assert field_2 != field_3


def test_table_equality():
    config_1 = TableConfig(name="table")
    config_2 = TableConfig(name="other_table")
    table_1 = Table(config_1)
    table_2 = Table(config_1)
    table_3 = Table(config_2)

    assert table_1 == table_2
    assert table_2 != table_3


def test_row_count():
    table_config = TableConfig(name="table")
    field_config = FieldConfig(
        name="field", dtype=Integer, params={"lower_bound": 0, "upper_bound": 10}
    )
    field = Field(field_config)

    table = Table(table_config)
    table.add_field(field)
    table.populate()

    assert table.row_count == table.data.height


def test_to_csv():
    table_config = TableConfig(name="table")
    field_config = FieldConfig(
        name="field", dtype=Integer, params={"lower_bound": 0, "upper_bound": 10}
    )
    field = Field(field_config)

    table = Table(table_config)
    table.add_field(field)

    # Table intentionally not populated
    with pytest.raises(Exception):
        table.to_csv("out.csv")


def test_add_field():
    table_config = TableConfig(name="table")
    field_config = FieldConfig(
        name="field", dtype=Integer, params={"lower_bound": 0, "upper_bound": 10}
    )
    field = Field(field_config)

    table = Table(table_config)

    assert len(table.fields) == 0

    table.add_field(field)

    assert len(table.fields) == 1
    assert field.name in table.field_map
