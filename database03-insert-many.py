"""
database insert many records
"""
import sqlite3

# conn = sqlite3.connect(':memory:')   # if we just want an in memory database means temp and not saved
# Connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# insert many
many_customers = [('Jeff', 'Ballinger', 'jeff@jeff.com'),
                  ('Tony', 'Stark', 'ironman@email.com'),
                  ('Steve', 'Rodgers', 'captain@email.com'),
                  ('Natasha', 'Romanoff', 'Nat@email.com'),
                  ('Dan', 'deMann', 'Dan@email.com'),
                  ('Houston', 'Alexandreyiv', 'Alexh@email.com'),
                  ('Katryn', 'Valvanoff', 'Kat@email.com')
                  ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# commit our command
conn.commit()

# close the connectionh
conn.close()
