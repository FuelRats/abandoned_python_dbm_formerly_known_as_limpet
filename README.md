# Limpet

This project is under current development, and is intended as an async database connection manager specifically for [mechasqueak3](https://github.com/FuelRats/pipsqueak3).

However, it does have applications as a standalone, simple database query tool with a simple connection pool.

> Limpet is an asynchronous library, and its coroutine **must be awaited**!


This project is currently in *pre-release*.  Use at your own risk!

### Requirements
* Python 3.7+
* psycopg2 (available via ``pipenv install psycopg``
* A postgreSQL database (9.5+)


### Installation
This is python library.  Install using pip/pipenv
and import the DatabaseManager with ``from limpet import DatabaseManager``


### Usage
Create the DatabaseManager:

```
        >>> DatabaseManager(dbhost='DatabaseServer.org',
        ...                 dport=5432,
        ...                 dbname='DatabaseName',
        ...                 dbuser='DatabaseUserName',
        ...                 dbpassword='UserPassword')

```

*and* query the database using:

``await DatabaseManager.query(query, values)``

* *query* expects a psycopg2.sql.SQL composed object ([details](http://initd.org/psycopg/docs/sql.html))
* *values* is a tuple containing (in order) the values used in the query object.

.query() returns a *list* object, containing a tuple for each row result.

**If there are no results, the list will be empty.**

That's it.

### License

*Limpet* is licensed under the BSD 3-Clause License.

