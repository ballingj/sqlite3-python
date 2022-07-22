import db_app00 as db

# Add a record to the database
#db.add_one("Clint", "Barton", "Nighthawk@email.com")

# add Many records
new_heroes = [
    ('Peter', 'Parker', 'spidey@email.com'),
    ('Bucky', 'Barnes', 'wintersoldier@email.com'),
    ('Bruce', 'Banner', 'hulk@email.com')
]

db.add_many(new_heroes)

db.show_all()
