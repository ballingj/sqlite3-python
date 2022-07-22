"""
database delete records
"""
import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# delete records
c.execute("DELETE from customers WHERE rowid = 9")
c.execute("DELETE from customers WHERE rowid = 10")
c.execute("DELETE from customers WHERE rowid = 11")


# commit our command
conn.commit()

# query the database
c.execute("SELECT rowid, * FROM customers")

""" after the query, fetch the data in one of three ways
c.fetchone()    # will return the first record
c.fetchmany(3)  # pass in a value of how many to fetch
c.fetchall()    # will return a  of tuples
"""
# fetch all and save in variable
items = c.fetchall()

for item in items:
    print(item)

# close the connectionh
conn.close()
