from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.books import Book  # Import the book model
import requests

# Create a Blueprint for the book API
Book_api = Blueprint('book_api', __name__, url_prefix='/api/book')

# Create the API instance
api = Api(Book_api)

class BookAPI:
    class _Create(Resource):
        def post(self):
            # Get request JSON data
            body = request.get_json()

            # Extract Book information
            author = body.get('author')
            year = body.get('year')
            price = body.get('price')
            genre = body.get('genre')
            summary = body.get('summary')

            # Create a new Book object
            Book_obj = Book(author=author, year=year, price=price, genre=genre, summary=summary)

#2: Key Code block to add Book to database 
            # create Book in database
            book = book_obj.create()
            # success returns json of book
            if book:
                return jsonify(book.read())
            # failure returns error
            return {'message': f'Invalid input, correct fields should be author, year, price, genre, and summary'}, 400

            
    class _Read(Resource):
        def get(self):
        # Retrieve all Books from the database
            Books = Books.query.all()
            json_ready = [book.to_dict() for book in Books]
        # Return the JSON response
            return jsonify(json_ready)

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
