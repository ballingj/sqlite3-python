## SQLAlchemy Core

Activate venv
> see first part of Flask Cheatsheet

Install SQLalchemy
```sh
pip install sqlalchemy
```

### Caution: Always Use Parameters when using text()
- When using text() do not build strings Dynamically

```python
** NO! **
text(f"INSERT INTO person (last_name, ) VALUES ({ln}, )")

# YES
text("INSERT INTO person (last_name, ) VALUES (:ln, )")
```

### SQLAlchemy: Connection
```python
# Connecting
from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///./data/books.db", echo=True, future=True)

conn = engine.connect()

```

### SQLAlchemy: Core TEXT
```python
# continuation of codes after connection object 'conn' is made
result = conn.execute(text("select * from author"))
print(result.all())
# -> [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy')]

 # Execute
conn.execute(
    text("INSERT INTO author (first_name, last_name) VALUES (:fn, :ln)"),
    [{"fn":"Tom", "ln":"Clancy"}, {"fn":"Stephen", "ln":"King"}]
    )
# 2022-05-17 08:48:20,373 INFO sqlalchemy.engine.Engine INSERT INTO author (first_name, last_name) VALUES (?, ?)
# 2022-05-17 08:48:20,373 INFO sqlalchemy.engine.Engine [generated in 0.00014s] (('Tom', 'Clancy'), ('Stephen', 'King'))
# <sqlalchemy.engine.cursor.CursorResult object at 0x110736fe0>

result = conn.execute(text("select * from author"))
# 2022-05-17 08:48:43,317 INFO sqlalchemy.engine.Engine select * from author
# 2022-05-17 08:48:43,317 INFO sqlalchemy.engine.Engine [cached since 334.4s ago] ()
print(result.all())
# [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy'), (4, 'Stephen', 'King')]

# Commits
conn.commit()

# Rollbacks
conn.execute(
text("INSERT INTO author (first_name, last_name) VALUES (:fn, :ln)"),
    [{"fn":"Not", "ln":"Anauthor"}, ]
    )
# 2022-05-17 08:51:18,204 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2022-05-17 08:51:18,204 INFO sqlalchemy.engine.Engine INSERT INTO author (first_name, last_name) VALUES (?, ?)
#2022-05-17 08:51:18,204 INFO sqlalchemy.engine.Engine [generated in 0.00019s] ('Not', 'Anauthor')
# sqlalchemy.engine.cursor.CursorResult object at 0x110737490>
result = conn.execute(text("select * from author"))
# 2022-05-17 08:51:25,900 INFO sqlalchemy.engine.Engine select * from author
# 2022-05-17 08:51:25,900 INFO sqlalchemy.engine.Engine [cached since 496.8s ago] ()%% ago] ()
print(result.all())
# [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy'), (4, 'Stephen', 'King'), (5, 'Not', 'Anauthor')]
conn.rollback()
# 2022-05-17 08:51:33,965 INFO sqlalchemy.engine.Engine ROLLBACK
result = conn.execute(text("select * from author"))
# 2022-05-17 08:51:36,133 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2022-05-17 08:51:36,133 INFO sqlalchemy.engine.Engine select * from author
# 2022-05-17 08:51:36,133 INFO sqlalchemy.engine.Engine [cached since 507s ago] ()
print(result.all())
# [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy'), (4, 'Stephen', 'King')]
```

Formatting Output
```python
# Query Results
result = conn.execute(text("select * from author"))
# 2022-05-17 08:54:45,306 INFO sqlalchemy.engine.Engine select * from author
# 2022-05-17 08:54:45,306 INFO sqlalchemy.engine.Engine [cached since 696.2s ago] ()
for row in result:
    print(f"{row.last_name}, {row.first_name}")

# Asimov, Isaac
# Buck, Pearl
# Clancy, Tom
# King, Stephen

print(result.all())
# []

result = conn.execute(text("select first_name, last_name from author"))
# 2022-05-17 08:57:29,295 INFO sqlalchemy.engine.Engine select first_name, last_name from author
# 2022-05-17 08:57:29,295 INFO sqlalchemy.engine.Engine [generated in 0.00014s] ()
for first_name, last_name in result:
    print(f"{first_name} of the clan {last_name}")

# Isaac of the clan Asimov
# Pearl of the clan Buck
# Tom of the clan Clancy
# Stephen of the clan King

result = conn.execute(text("select first_name, last_name from author"))
# 2022-05-17 08:58:42,153 INFO sqlalchemy.engine.Engine select first_name, last_name from author
# 2022-05-17 08:58:42,153 INFO sqlalchemy.engine.Engine [cached since 72.86s ago] ()

for row in result:
    print(row[1])
# Asimov
# Buck
# Clancy
# King

# Dictionary output
result = conn.execute(text("select first_name, last_name from author"))
# 2022-05-17 09:00:29,644 INFO sqlalchemy.engine.Engine select first_name, last_name from author
# 2022-05-17 09:00:29,644 INFO sqlalchemy.engine.Engine [cached since 180.3s ago] ()
for dict_row in result.mappings():
    print(dict_row)

# {'first_name': 'Isaac', 'last_name': 'Asimov'}
# {'first_name': 'Pearl', 'last_name': 'Buck'}
# {'first_name': 'Tom', 'last_name': 'Clancy'}
# {'first_name': 'Stephen', 'last_name': 'King'}

# Parameters
result = conn.execute(
    text("SELECT last_name FROM author WHERE last_name > :ln"),
    {"ln":"C"}
    )
# 2022-05-17 09:02:32,456 INFO sqlalchemy.engine.Engine SELECT last_name FROM author WHERE last_name > ?
# 2022-05-17 09:02:32,456 INFO sqlalchemy.engine.Engine [generated in 0.00014s] ('C',)
print(result.all())
# [('Clancy',), ('King',)]

stmt = text("SELECT last_name FROM author WHERE last_name > :ln")
stmt
# <sqlalchemy.sql.elements.TextClause object at 0x110737310>
```

Bindparams
```python
# bindparams
stmt = stmt.bindparams(ln="C")
result = conn.execute(stmt)
# 2022-05-17 09:05:03,565 INFO sqlalchemy.engine.Engine SELECT last_name FROM author WHERE last_name > ?
# 2022-05-17 09:05:03,565 INFO sqlalchemy.engine.Engine [generated in 0.00016s] ('C',)
print(result.all())
# [('Clancy',), ('King',)]
stmt = stmt.bindparams(ln="B")
result = conn.execute(stmt)
# 2022-05-17 09:05:19,565 INFO sqlalchemy.engine.Engine SELECT last_name FROM author WHERE last_name > ?
# 2022-05-17 09:05:19,565 INFO sqlalchemy.engine.Engine [cached since 16s ago] ('B',)
print(result.all())
[('Buck',), ('Clancy',), ('King',)]
```

Clean UP by closing the connections
```python
# Clean-up
conn.close()
```



### SQLAlchemy: Core Statement
> using the core text() option requires using raw SQL statements and manipulation of the results.  SQLAlchemy provides statements to abstract those away

### SQLAlchemy: Connection
```python
# Connect as before
from sqlalchemy import create_engine
engine = create_engine("sqlite:///./data/books.db", echo=True, future=True)

conn = engine.connect()
```

SQLAlchemy MetaData object
> sqlalchemy can keep a representation of database as an object
```python
# MetaData
from sqlalchemy import MetaData, Table
# create a metadata object
metadata = MetaData()
# grab table info about the authot table
author_table = Table("author", metadata, autoload_with=engine)
print(author_table)
# Table('author', MetaData(), Column('author_id', INTEGER(), table=<author>, primary_key=True, nullable=False), Column('first_name', VARCHAR(), table=<author>), Column('last_name', VARCHAR(), table=<author>), schema=None)

# Select 
from sqlalchemy import select
stmt = select(author_table).where(author_table.c.first_name == "Stephen")
print(stmt)
# SELECT author.author_id, author.first_name, author.last_name
# FROM author
# WHERE author.first_name = :first_name_1

result = conn.execute(stmt)
print(result.all())
# [(4, 'Stephen', 'King')]

print(select(author_table))
# SELECT author.author_id, author.first_name, author.last_name
# FROM author

print(select(author_table.c.first_name, author_table.c.last_name))
# SELECT author.first_name, author.last_name
# FROM author
stmt = select(author_table).where(author_table.c.last_name > "C")
str(stmt)
# 'SELECT author.author_id, author.first_name, author.last_name \nFROM author \nWHERE author.last_name > :last_name_1'

# Compiled SQL statement
compiled = stmt.compile()
str(compiled)
# 'SELECT author.author_id, author.first_name, author.last_name \nFROM author \nWHERE author.last_name > :last_name_1'
compiled.params
# {'last_name_1': 'C'}
result = conn.execute(compiled)
# 2022-05-17 09:29:46,203 INFO sqlalchemy.engine.Engine SELECT author.author_id, author.first_name, author.last_name FROM author WHERE author.last_name > ?
# 2022-05-17 09:29:46,203 INFO sqlalchemy.engine.Engine [generated in 0.00019s] ('C',)
print(result.all())
# [(3, 'Tom', 'Clancy'), (4, 'Stephen', 'King')]

# Multiple WHERE clause
stmt = select(author_table).where(author_table.c.last_name > "B",
		author_table.c.first_name > "S")
result = conn.execute(stmt)
# 2022-05-17 09:43:18,232 INFO sqlalchemy.engine.Engine SELECT author.author_id, author.first_name, author.last_name FROM author WHERE author.last_name > ? AND author.first_name > ?
# 2022-05-17 09:43:18,232 INFO sqlalchemy.engine.Engine [generated in 0.00015s] ('B', 'S')
print(result.all())
# [(3, 'Tom', 'Clancy'), (4, 'Stephen', 'King')]

```
Insert
```python
# Insert
from sqlalchemy import insert

stmt = insert(author_table).values(first_name="Richard", last_name="Bachman")
str(stmt)
# 'INSERT INTO author (first_name, last_name) VALUES (:first_name, :last_name)'

# Compiled version
compiled = stmt.compile()
>>> str(compiled)
# 'INSERT INTO author (first_name, last_name) VALUES (:first_name, :last_name)'
compiled.params
# {'first_name': 'Richard', 'last_name': 'Bachman'}
conn.execute(stmt)
# 2022-05-17 09:45:27,461 INFO sqlalchemy.engine.Engine INSERT INTO author (first_name, last_name) VALUES (?, ?)
# 2022-05-17 09:45:27,461 INFO sqlalchemy.engine.Engine [generated in 0.00016s] (('Richard', 'Bachman'))

conn.execute(select(author_table)).all()
# 2022-05-17 09:49:15,691 INFO sqlalchemy.engine.Engine SELECT author.author_id, author.first_name, author.last_name FROM author
# 2022-05-17 09:49:15,691 INFO sqlalchemy.engine.Engine [generated in 0.00016s] ()
# [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy'), (4, 'Stephen', 'King'), (5, 'Richard', 'Bachman')]

# insert multiple rows
result = conn.execute(
    insert(author_table),
    [ {"first_name":"John", "last_name":"Le Carre"}, {"first_name":"Alex", "last_name":"Michaelides"}]
    )

# Commit is same as before
conn.commit()

conn.execute(select(author_table)).all()
# [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy'), (4, 'Stephen', 'King'), (5, 'Richard', 'Bachman'), (6, 'John', 'Le Carre'), (7, 'Alex', 'Michaelides')]

```

Update
```python
# Update
from sqlalchemy import update
stmt = update(author_table).where(author_table.c.last_name ==
	"King").values(first_name='Stephen "The Ruler"')
conn.execute(stmt)
# 2022-05-17 10:01:31,026 INFO sqlalchemy.engine.Engine UPDATE author SET first_name=? WHERE author.last_name = ?
# 2022-05-17 10:01:31,026 INFO sqlalchemy.engine.Engine [generated in 0.00015s] ('Stephen "The Ruler"', 'King')
# <sqlalchemy.engine.cursor.CursorResult object at 0x10664e800>
conn.execute(select(author_table)).all()
# 2022-05-17 10:01:34,569 INFO sqlalchemy.engine.Engine SELECT author.author_id, author.first_name, author.last_name FROM author
# 2022-05-17 10:01:34,569 INFO sqlalchemy.engine.Engine [cached since 738.9s ago] ()
# [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy'), (4, 'Stephen "The Ruler"', 'King'), (5, 'Richard', 'Bachman'), (6, 'John', 'Le Carre'), (7, 'Alex', 'Michaelides')]

# Rollback the update
conn.rollback()
# 2022-05-17 10:01:41,169 INFO sqlalchemy.engine.Engine ROLLBACK
conn.execute(select(author_table)).all()
# 2022-05-17 10:01:43,489 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2022-05-17 10:01:43,489 INFO sqlalchemy.engine.Engine SELECT author.author_id, author.first_name, author.last_name FROM author
# 2022-05-17 10:01:43,489 INFO sqlalchemy.engine.Engine [cached since 747.8s ago] ()
# [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy'), (4, 'Stephen', 'King'), (5, 'Richard', 'Bachman'), (6, 'John', 'Le Carre'), (7, 'Alex', 'Michaelides')]

```
Delete
```python
# Delete
from sqlalchemy import delete
stmt = delete(author_table).where(author_table.c.author_id == 7)
conn.execute(stmt)
# 2022-05-17 10:03:51,408 INFO sqlalchemy.engine.Engine DELETE FROM author WHERE author.author_id = ?
# 2022-05-17 10:03:51,408 INFO sqlalchemy.engine.Engine [generated in 0.00015s] (7,)
# <sqlalchemy.engine.cursor.CursorResult object at 0x107d7db40>
conn.execute(select(author_table)).all()
# 2022-05-17 10:03:57,776 INFO sqlalchemy.engine.Engine SELECT author.author_id, author.first_name, author.last_name FROM author
# 2022-05-17 10:03:57,776 INFO sqlalchemy.engine.Engine [cached since 882.1s ago] ()
# [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy'), (4, 'Stephen', 'King'), (5, 'Richard', 'Bachman'), (6, 'John', 'Le Carre')]

# Rollback the delete
conn.rollback()
# 2022-05-17 10:04:03,191 INFO sqlalchemy.engine.Engine ROLLBACK
conn.execute(select(author_table)).all()
# 2022-05-17 10:04:05,879 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2022-05-17 10:04:05,879 INFO sqlalchemy.engine.Engine SELECT author.author_id, author.first_name, author.last_name FROM author
# 2022-05-17 10:04:05,880 INFO sqlalchemy.engine.Engine [cached since 890.2s ago] ()
# [(1, 'Isaac', 'Asimov'), (2, 'Pearl', 'Buck'), (3, 'Tom', 'Clancy'), (4, 'Stephen', 'King'), (5, 'Richard', 'Bachman'), (6, 'John', 'Le Carre'), (7, 'Alex', 'Michaelides')]

```

Ref:
https://realpython.com/courses/sqlite-sqlalchemy-python/
https://realpython.com/python-sqlite-sqlalchemy/
