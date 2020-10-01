from collections import namedtuple
from dataclasses import dataclass


Databases = namedtuple('Database', 'postgres redis')