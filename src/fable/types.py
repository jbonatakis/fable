import datetime

from . import generators


class FableType:
    """This class exists solely to be subclassed for type checking purposes"""

    pass


class Integer(FableType):
    dtype = int
    generator = generators.NumericGenerator


class Varchar(FableType):
    dtype = str
    generator = generators.StringGenerator


class Date(FableType):
    dtype = datetime.date
    generator = generators.DateGenerator
