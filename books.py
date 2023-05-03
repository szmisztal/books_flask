from app import app, db
from app.models import Book, Author, Bookcase, book_author

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": Book,
       "Author": Author,
       "Bookcase": Bookcase,
       "book_author": book_author
   }
