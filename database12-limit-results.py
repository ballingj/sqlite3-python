"""
database limiting results
"""
import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# query the database - LIMITS results
#c.execute("SELECT rowid, * FROM customers LIMIT 3")
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")

""" after the query, fetch the data in one of three ways
c.fetchone()    # will return the first record
c.fetchmany(3)  # pass in a value of how many to fetch
c.fetchall()    # will return a  of tuples
"""
# fetch all and save in variable
items = c.fetchall()

for item in items:
    print(item)


# commit our command
conn.commit()

# close the connectionh
conn.close()
