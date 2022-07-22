"""
database query the database
"""
import sqlite3

# conn = sqlite3.connect(':memory:')   # if we just want an in memory database means temp and not saved
# Connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")

""" after the query, fetch the data in one of three ways
c.fetchone()    # will return the first record
c.fetchmany(3)  # pass in a value of how many to fetch
c.fetchall()    # will return a list
"""
# let's fetch all
print(c.fetchall())
# print(c.fetchone())
# print(c.fetchmany(3))

# commit our command
conn.commit()

# close the connectionh
conn.close()
