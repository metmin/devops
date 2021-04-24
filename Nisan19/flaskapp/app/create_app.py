from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)
    client = MongoClient('mongodb://mongodb:27017/')
    db = client.test_database

    @app.route('/')
    def index():
        headers = request.headers
        if request.headers.get('bootcamp') == 'devops':
            return render_template('index.html')
        else:
            return "Mehmet Emin Bora"

    @app.route('/users')
    def users():
        if request.headers.get('bootcamp') == 'devops':
            return render_template('index.html')
        else:
            collection = db.users.find()

            item = {}
            data = []
            for element in collection:
                item = {
                    'id': str(element['_id']),
                    'name': element['name'],
                    'lastname': element['lastname']
                }
                data.append(item)

            return jsonify(
                data=data
            )

    @app.route('/user')
    def user():
        if request.headers.get('bootcamp') == 'devops':
            return render_template('index.html')
        else:
            name = request.args.get('name')
            lastname = request.args.get('lastname')
            user = {
                'name': name,
                'lastname': lastname
            }
            db.users.insert_one(user)

            return 'Saved!', 201

    return app
