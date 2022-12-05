# published.py
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()

author_publisher = Table(
    "author_publisher",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("author.author_id")),
    Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
)

book_publisher = Table(
    "book_publisher",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("book.book_id")),
    Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
)

class Author(Base):
    __tablename__ = "author"

    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    books = relationship("Book", backref=backref("author"), 
        cascade="all, delete-orphan")

    publishers = relationship("Publisher", secondary=author_publisher,
        back_populates="authors")

    def __repr__(self):
        return (
            f"Author(author_id={self.author_id!r}, "
            f"first_name={self.first_name!r}, last_name={self.last_name!r})"
        )
    
class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("author.author_id"), nullable=False)

    publishers = relationship("Publisher", secondary=book_publisher,
        back_populates="books")

    def __repr__(self):
        return (
            f"Book(book_id={self.book_id!r}, "
            f"title={self.title!r}, author_id={self.author_id!r})"
        )

class Publisher(Base):
    __tablename__ = 'publisher'

    publisher_id = Column(Integer, primary_key=True)
    name = Column(String)

    authors = relationship("Author", secondary=author_publisher,
        back_populates="publishers")
    books = relationship("Book", secondary=book_publisher,
        back_populates="publishers")

    def __repr__(self):
        return (
            f"Publisher(publisher_id={self.publisher_id!r}, "
            f"name={self.name!r})"
        )



