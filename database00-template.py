"""
database template
"""
import sqlite3

# conn = sqlite3.connect(':memory:')   # if we just want an in memory database means temp and not saved
# Connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

#
c.execute()

# commit our command
conn.commit()

# close the connectionh
conn.close()
