"""
database insert a record into the cutomer table
"""
import sqlite3

#conn = sqlite3.connect(':memory:')   # if we just want an in memory database means temp and not saved
# Connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

# insert one record
c.execute("INSERT INTO customers VALUES ('Jeff', 'Ballinger', 'jeff@jeff.com')")

# commit our command
conn.commit()

# close the connectionh
conn.close()
