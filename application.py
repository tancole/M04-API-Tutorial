from flask import Flask
app = (__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(80), unique = True)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

def __repr__(self):
    return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Books.query.all()

    output = []
    for book in books:
        books_data = {'name': books.name, 'description': books.description}
        output.append(books_data)

    return {"books": output}

@app.route('/books/<id>')
def get_books(id):
    books = Books.query.get_or_404(id)
    return {"name": books.name, "description": books.description}

@app.route('/books/<author>')
def get_books(author):
    books = Books.query.get_or_404(author)
    reutrn {"name": books.name, "description": books.description}

@app.route('/books/<publisher>')
def get_books(publisher):
    books = Books.query.get_or_404(publisher)
    return {"name": books.name, "description": books.description}

@app.route('/books', methods=['POST'])
def add_books():
    books = Books(name = request.json['name'], description = request.json['description'])
    db.session.add(books)
    db.session.commit()
    return {'id': books.id}

@app.route('/books/<id>', methods = ['DELTE'])
def delete_books(id):
    books = Books.query.get(id)
    if books is None:
        return {"Error": "Not Found"}
    db.session.delete(books)
    db.session.commit()
    return {'message': 'Thank you.'}

