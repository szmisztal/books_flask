A simple flask app to practice with SQL databases.

Put all files in one folder,

turn on the terminal, 

create a virtual environment and install modules with: pip install -r requirements.txt

flask shell run

to add book use:

    b = Book(title, year_of_publication, genre, short_description)

    db.session.add(b)

    db.session.commit()
    
to add author use:
    
    a = Author(first_name, last_name, birth_date, death_date)   # death_date is not required
    
    db.session.add(a)
    
    db.session.commit()
    
to add book status use:

    c = Bookcase(book_id, status, who_borrowed)    # if book isn`t borrowed, ignore who_borrowed
    
    db.session.add(c)
    
    db.session.commit()
    
to add book to author use:

    a = Author.query.get(author_id)
    
    b = Book.query.get(book_id)
    
    a.books.append(b)
    
    db.session.commit()    # similarly, you can add an author to a book by swapping variables
 
