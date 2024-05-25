import datetime

from . import generators


class FableType:
    pass


class Integer(FableType):
    dtype = int
    generator = generators.NumericGenerator


class Varchar(FableType):
    dtype = str
    generator = generators.VarcharGenerator


class Date(FableType):
    dtype = datetime.date
    generator = generators.DateGenerator
