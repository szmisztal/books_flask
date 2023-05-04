from flask import render_template, request, redirect, url_for
from app import db
from app import app
from app.models import Book, Author, Bookcase, book_author
@app.route('/')
def home():
    return render_template('head.html')

@app.route('/books', methods = ['GET', 'POST'])
def books():
    books = Book.query.all()
    if request.method == 'GET':
        return render_template("books.html", books = books)
    elif request.method == 'POST':
        title = request.form['title']
        year_of_publication = request.form['year_of_publication']
        genre = request.form['genre']
        short_description = request.form['short_description']
        new_book = Book(title = title, year_of_publication = year_of_publication, genre = genre, short_description = short_description)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books'))

@app.route('/authors', methods = ['GET', 'POST'])
def authors():
    authors = Author.query.all()
    if request.method == 'GET':
        return render_template("authors.html", authors = authors)
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        death_date = request.form['death_date']
        new_author = Author(first_name = first_name, last_name = last_name, birth_date = birth_date, death_date = death_date)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('authors'))

@app.route('/bookcase', methods = ['GET', 'POST'])
def bookcase():
    bookcase = Bookcase.query.all()
    books = Book.query.all()
    if request.method == 'GET':
        return render_template("bookcase.html", bookcase = bookcase, books = books)
    elif request.method == 'POST':
        book_id = request.form['book_id']
        status = request.form['status']
        who_borrowed = request.form['who_borrowed']
        new_bookcase = Bookcase(book_id = book_id, status = status, who_borrowed = who_borrowed)
        db.session.add(new_bookcase)
        db.session.commit()
        return redirect(url_for('bookcase'))

@app.route('/book_author', methods = ['GET', 'POST'])
def add_book_author():
    books = Book.query.all()
    authors = Author.query.all()
    if request.method == 'GET':
        return render_template("book_author.html", books = books, authors = authors)
    elif request.method == 'POST':
        book_id = request.form['book']
        author_id = request.form['author']
        book = Book.query.get(book_id)
        author = Author.query.get(author_id)
        book.authors.append(author)
        db.session.commit()
        return render_template('head.html')
