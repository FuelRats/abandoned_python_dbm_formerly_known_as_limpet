"""
__init__.py

Limpet - async PostgreSQL wrapper for psycopg2.

Copyright (c) 2018 The Fuel Rat Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.
See LICENSE.md
"""
from .database_manager import DatabaseManager
__all__ = ["DatabaseManager"]
