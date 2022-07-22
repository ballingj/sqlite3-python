"""
database and or
"""
import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# query the database - AND/OR - allows to extend functionality of WHERE clause
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Ro%' ")
#c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%at%' ")
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Ro%' AND email LIKE '%at%' ")
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Ro%' OR email LIKE '%at%' ")


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
