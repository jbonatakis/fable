from abc import ABC, abstractclassmethod
import logging
import random
from typing import List

logger = logging.getLogger(__name__)


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

    @classmethod
    def generate(cls, row_count: int, params: dict) -> List[int]:
        cls._validate_params(params)
        values = []
        for _ in range(row_count):
            values.append(cls._generate_value(params))
        return values

    @classmethod
    def _generate_value(cls, params):
        return random.randint(params["lower_bound"], params["upper_bound"])

    @classmethod
    def _validate_params(cls, params):
        for k, v in params.items():
            if k not in cls.required_params:
                # TODO: Figure out logging
                # logger.warn(
                #     f"Found {k} in params, but it is not required for this generator"
                # )
                continue
            if not isinstance(v, cls.required_params[k]):
                raise TypeError(
                    f"Expected {k} to be of type {cls.required_params[k]}, but got {v.__class__}"
                )


class VarcharGenerator(AbstractBaseGenerator):
    pass


class DateGenerator(AbstractBaseGenerator):
    pass
