"""
Create a database and a table
"""
import sqlite3

# conn = sqlite3.connect(':memory:')   # if we just want an in memory database means temp and not saved
# Connect to database (if non exist, then create the customer.db)
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# create a table (sqlite3 only has 5 datatypes: NULL, INTEGER, REAL, TEXT, BLOB
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
        )
""")

# commit our command
conn.commit()

# close the connectionh
conn.close()
