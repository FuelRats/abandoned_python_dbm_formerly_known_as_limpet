"""
database_manager.py - Provides database connectivity.


Copyright (c) 2018 The Fuel Rat Mischief,
All rights reserved.
Licensed under the BSD 3-Clause License.
See LICENSE.md
"""
from psycopg2 import sql, pool
import psycopg2


class DatabaseManager(object):

    def __init__(self,
                 dbhost=None,
                 dbport=None,
                 dbname=None,
                 dbuser=None,
                 dbpassword=None
                 ):

        #####
        # Class properties
        ###
        self._dbhost = dbhost
        self._dbport = dbport
        self._dbname = dbname
        self._dbuser = dbuser
        self._dbpass = dbpassword

        #####
        # Assert that properties are set:
        ###
        assert self._dbhost
        assert self._dbport
        assert self._dbname
        assert self._dbuser
        assert self._dbpass

        ######
        # Create Database Connection Pool
        ###
        try:
            self._pool = psycopg2.pool.SimpleConnectionPool(1, 10, host=self._dbhost,
                                                            port=self._dbport,
                                                            dbname=self._dbname,
                                                            user=self._dbuser,
                                                            password=self._dbpass)

        except psycopg2.DatabaseError as error:
            raise error

        async def query(self, sql_query: sql.SQL, values: tuple) -> list:
            """
             Send a query to the connected database.  Pulls a connection from the pool
             and creates a cursor, executing the composed query with the values.

             Requires a composed SQL object (See psycopg2 docs)
             Args:
                 self: self
                 sql_query: composed SQL query object
                 values: tuple of values for query
             Returns:
                 List of rows matching query.  May return an empty list if there are
                 no matching rows.
             """
            # Verify composed SQL object
            if not isinstance(sql_query, sql.SQL):
                raise TypeError("Expected composed SQL object for query.")

            # Verify value is tuple
            if not isinstance(values, tuple):
                raise TypeError("Expected tuples for query values.")

            with self._dbpool.getconn() as connection:
                connection.autocommit = True
                connection.set_client_encoding('utf-8')

                with connection.cursor() as cursor:
                    cursor.execute(sql_query, values)
                    result = cursor.fetchall()

            self._dbpool.putconn(connection)

            return list(result)
