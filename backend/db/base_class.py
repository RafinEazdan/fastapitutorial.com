from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative
"""
from typing import Any
Imports Any type hint, which means “any type of value” in Python type annotations.

from sqlalchemy.ext.declarative import declared_attr
Imports declared_attr, a decorator used in SQLAlchemy models to define attributes that are calculated dynamically for each subclass (often used for things like __tablename__).

from sqlalchemy.orm import as_declarative
Imports as_declarative, a decorator that turns a base class into a SQLAlchemy declarative base, so you can define ORM models by inheriting from it.
"""

@as_declarative()
class Base:
    id: Any
    __name__: str
    
    #generating the tablename from class name
    '''
    All your model classes will inherit from a common Base class, which helps SQLAlchemy know how to map your classes to database tables.


    A DB model is a Python class that represents a table in a database.

    Each model = one table.
    Each attribute = one column.
    Usually, one model should represent one table.
    You should not have multiple models for the same table, because it can cause confusion and bugs.
    '''

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()