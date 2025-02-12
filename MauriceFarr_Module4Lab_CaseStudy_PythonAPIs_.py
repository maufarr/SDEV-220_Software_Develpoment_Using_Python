"""
author: Maurice Farr
date: 2/5/2025
assignment: Module 4 Lab - Case Study: Python APIs
purpose: We need to examine Python APIs and database interaction. After viewing the video, we have to develop a CRUD API for a Book
rather than a Drink as demonstrated in the example. The Book model must include the following attributes: id, book_name, author, and publisher.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db' # The database that we will retrieve the books from
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Book {self.book_name}>'

# Ensure tables are created before the first request
with app.app_context():
    db.create_all()

# CRUD Operations

# Create a new book
@app.route('/book', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        book_name=data['book_name'],
        author=data['author'],
        publisher=data['publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully!'}), 201

# Read all books
@app.route('/book', methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = [{"id": book.id, "book_name": book.book_name, "author": book.author, "publisher": book.publisher} for book in books]
    return jsonify(books_list), 200

# Read a single book by ID
@app.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    }), 200

# Update a book by ID
@app.route('/book/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)

    db.session.commit()
    return jsonify({'message': 'Book updated successfully!'}), 200

# Delete a book by ID
@app.route('/book/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully!'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)