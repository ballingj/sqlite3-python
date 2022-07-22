import db_app00 as db

# Add a record to the database
#db.add_one("Clint", "Barton", "Nighthawk@email.com")

# delete a record using rowid as string
db.delete_one('10')

db.show_all()
