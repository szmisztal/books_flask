from app import db

book_author = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key = True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key = True)
    )

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), index = True, unique = True)
    year_of_publication = db.Column(db.Integer, index = True)
    genre = db.Column(db.String(30), index = True)
    short_description = db.Column(db.String(200))
    authors = db.relationship('Author', secondary = 'book_author', backref = 'Books', lazy = 'dynamic')

    def __str__(self):
        return f"{self.authors}, {self.title}, {self.year_of_publication}, {self.genre}, {self.short_description}"

class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(50), index = True)
    birth_date = db.Column(db.String(20))
    death_date = db.Column(db.String(20), nullable = True)
    books = db.relationship('Book', secondary = 'book_author', backref = 'Authors', lazy = 'dynamic')

    def __str__(self):
        if self.death_date is None:
            return f"{self.first_name}, {self.last_name}, {self.books}, birth date: {self.birth_date}"
        else:
            return f"{self.first_name}, {self.last_name}, {self.books}, birth date: {self.birth_date}, death date: {self.death_date}"

class Bookcase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book', backref = 'bookcases', lazy = 'select')
    status = db.Column(db.String(10), index = True)
    who_borrowed = db.Column(db.String(50), index = True, nullable = True)

    def __str__(self):
        if self.who_borrowed is None:
            return f"The {self.book} is on the shelf"
        else:
            return f"The {self.book} is borrowed by {self.who_borrowed}"


