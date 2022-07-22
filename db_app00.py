"""
database module for the db_app.py
"""
import sqlite3

####### Functions show_all in Here #######
#Query the database and return all
def show_all():
    # Connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    # Query the database
    c.execute("SELECT rowid, * FROM customers")

    # fetch all and save in variable
    items = c.fetchall()

    # print the result
    for item in items:
        print(item)

    # commit and close
    conn.commit()
    conn.close()


####### Functions add_one in Here #######
# Add a new record to a table
def add_one(first, last, email):
    # Connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    # commit and close
    conn.commit()
    conn.close()

###### Function Add Many in Here ###############
# Add many records - list
def add_many(list):
    # Connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    # commit and close
    conn.commit()
    conn.close()


####### Function delete_one in Here ###############
# delete a record
def delete_one(id):
    # Connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    #c.execute("DELETE from customers WHERE rowid = (?)", id)   # I heard this causes problems for two or more digits- solution is pass a tuple
    c.execute("DELETE from customers WHERE rowid = (?)", (id,))

    # commit and close
    conn.commit()
    conn.close()


####### Function delete_one in Here ###############
# delete a record
def email_lookup(email):
    # Connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))

    # fetch all and save in variable
    items = c.fetchall()

    # print the result
    for item in items:
        print(item)

    # commit and close
    conn.commit()
    conn.close()
