"""
database query using where clause
"""
import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# Query the database
#c.execute("SELECT * FROM customers WHERE last_name = 'Rodgers'")
# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Rod%'")    # % here is a wildcard
c.execute("SELECT * FROM customers WHERE email LIKE '%email.com'")

""" after the query, fetch the data in one of three ways
c.fetchone()    # will return the first record
c.fetchmany(3)  # pass in a value of how many to fetch
c.fetchall()    # will return a list
"""
# fetch all and save in variable
items = c.fetchall()

for item in items:
    print(item)

# commit our command
conn.commit()

# close the connectionh
conn.close()
