
# import libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView

# create an instance of Flask
app = Flask(__name__)
# configures the app with the database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# create database
db = SQLAlchemy(app)

# define models
# a model for a Person
class Person(db.Model):
    # define columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)

    # representation of a Person object
    def __repr__(self):
        return '<Person %r>' % self.name

# a model for a Pet
class Pet(db.Model):
    # define columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(80))

    # representation of a Pet object
    def __repr__(self):
        return '<Pet %r>' % self.name

# define schema
schema = Schema(query=Query)

# add GraphQL view
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# run the app
if __name__ == '__main__':
    app.run()
