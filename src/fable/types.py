import datetime

from . import generators


class Integer:
    dtype = int
    generator = generators.NumericGenerator


class Varchar:
    dtype = str
    generator = generators.VarcharGenerator


class Date:
    dtype = datetime.date
    generator = generators.DateGenerator
