## SQLAlchemy: ORM

###### SQLAlchemy: ORM Connection
```python
# Connecting
from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///./data/books.db", echo=True, future=True)

# we use Sessions in orm - define the session object
from sqlalchemy.orm import Session
session = Session(engine)

# import the models ( see code for models.py)
from models import Author, Book
```

Working with select in Session
```python
from sqlalchemy import select, 
stmt = select(Author)
for author in session.scalars(stmt):
    print(author)
# Author(author_id=1, first_name='Isaac', last_name='Asimov')
# Author(author_id=2, first_name='Pearl', last_name='Buck')
# Author(author_id=3, first_name='Tom', last_name='Clancy')
# Author(author_id=4, first_name='Stephen', last_name='King')
# Author(author_id=5, first_name='Richard', last_name='Bachman')
# Author(author_id=6, first_name='John', last_name='Le Carre')
# Author(author_id=7, first_name='Alex', last_name='Michaelides')

stmt = select(Book)
for book in session.scalars(stmt):
    print(book)
# Book(book_id=1, title='Foundation', author_id=1)
# Book(book_id=2, title='The Good Earth', author_id=2)

stmt = select(Book).join(Book.author).where(Author.last_name > "B")
for book in session.scalars(stmt):
    print(book)
# Book(book_id=2, title='The Good Earth', author_id=2)

stmt = select(Author).where(Author.last_name == "King")
king = session.scalars(stmt).one()
print(king)
# Author(author_id=4, first_name='Stephen', last_name='King')

# Using the new "king" object to add a book to collection
king.books.append(Book(title="It"))

print(session.scalars(select(Book)).all())
# [Book(book_id=1, title='Foundation', author_id=1), Book(book_id=2, title='The Good Earth', author_id=2), Book(book_id=None, title='It', author_id=None)]
print(king.books) # notice the id = None ( need to be commited)
# [Book(book_id=None, title='It', author_id=None)]

# this is the same as using a where clause - we are asking for auhhor who is primary key is '4' 
king = session.get(Author, 4)
```

Inserting (add & append)
```python
# Adding is for object - adds a new author to the table Author
author = Author(first_name="Robert", last_name="Ludlum")
session.add(author)
session.scalars(select(Author)).all()
# [Author(author_id=1, first_name='Isaac', last_name='Asimov'), Author(author_id=2, first_name='Pearl', last_name='Buck'), Author(author_id=3, first_name='Tom', last_name='Clancy'), Author(author_id=4, first_name='Stephen', last_name='King'), Author(author_id=5, first_name='Robert', last_name='Ludlum')]

# appending is for relations - adding a book to author
king.books.append(Book(title="Dead Zone"))
print(king.books)  # notice the ids still = None
# [Book(book_id=None, title='It', author_id=None), Book(book_id=None, title='Dead Zone', author_id=None)]

# Commit 
session.commit()

```

Removing and Deleting
```python
# Remove is used for related things
king.books.remove(king.books[1])

print(king.books)  # book 'deadzone' was removed & id is now populated as a result of the commit
# [Book(book_id=3, title='It', author_id=4)]

# Delete is used for objects - this will delete king the author and all his books due to "Cascade" clause in the models
session.delete(king)
print(session.scalars(select(Book)).all())
# [Book(book_id=1, title='Foundation', author_id=1), Book(book_id=2, title='The Good Earth', author_id=2)]

# Rollback
session.rollback()
session.close()

```

### models.py
```python
# models.py
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()

class Author(Base):
    __tablename__ = "author"

    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    books = relationship("Book", backref=backref("author"), 
        cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"Author(author_id={self.author_id}, "
            f"first_name={self.first_name}, last_name={self.last_name})"
        )

class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("author.author_id"), nullable=False)

    def __repr__(self):
        return (
            f"Book(book_id={self.book_id!r}, "
            f"title={self.title!r}, author_id={self.author_id!r})"
        )
```


