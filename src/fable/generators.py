from abc import ABC, abstractclassmethod
import logging
import random
from typing import List

import faker

class AbstractBaseGenerator(ABC):
    @abstractclassmethod
    def generate():
        pass

    @abstractclassmethod
    def _generate_value():
        pass

    @abstractclassmethod
    def _validate_params():
        pass


class NumericGenerator(AbstractBaseGenerator):
    required_params = {"lower_bound": int, "upper_bound": int}
    # bound_range = required_params.get("lower_bound") + required_params.get(
    #     "upper_bound"
    # )
    # default_params = {
    #     "mean": bound_range / 2,
    #     "sigma": bound_range / 10,
    # }

    @classmethod
    def generate(cls, row_count: int, params: dict) -> List[int]:
        cls._validate_params(params)
        values = []
        for _ in range(row_count):
            values.append(cls._generate_value(params))
        return values

    @classmethod
    def _generate_value(cls, params) -> int:
        # TODO: properly return a value based on provided params
        if isinstance(params.get("distribution"), str):
            distribution = params.get("distribution").lower()
            if distribution == "normal":
                return round(random.normalvariate(5000, 1))
        return random.randint(params["lower_bound"], params["upper_bound"])

    @classmethod
    def _validate_params(cls, params):
        """Parameter validation for this generator is based on the existence and value of the `distribution` parameter."""
        # TODO: Update validation to look at `distribution` param.
        # If it doesn't exist, default to uniform distribution. Require `lower_bound` and `upper_bound`
        # If it does exist, require params based on distribution type
        # These params get passed in to the FieldConfig when defining a new field
        for k, v in params.items():
            if k not in cls.required_params:
                logging.warning(f"Found {k} in params, but it is not required for this generator")
                continue
            if not isinstance(v, cls.required_params[k]):
                raise TypeError(
                    f"Expected {k} to be of type {cls.required_params[k]}, but got {v.__class__}"
                )


class StringGenerator(AbstractBaseGenerator):
    
    @classmethod
    def generate(cls, row_count: int, params: dict) -> List[str]:
        cls._validate_params(params)
        values = []
        for _ in range(row_count):
            values.append(cls._generate_value(params))
        return values

    @classmethod
    def _generate_value(cls, params):
        return faker.Faker(use_weighting=False).name()

    @classmethod
    def _validate_params(cls, params):
        pass


class DateGenerator(AbstractBaseGenerator):
    pass
