"""
database order by
"""
import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# query the database - ORDER BY
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid ASC")   #ASC is default
c.execute("SELECT rowid, * FROM customers ORDER BY last_name ASC") 


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
