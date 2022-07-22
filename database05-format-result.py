"""
database query; fetch; format
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
# print(c.fetchone())
# print(c.fetchmany(3))

# let's fetch all and save in variable
items = c.fetchall()

for item in items:
    print(f"{item[0]} {item[1]} | {item[2]}")

# commit our command
conn.commit()

# close the connectionh
conn.close()
