from flask import Flask
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

from app_settings import DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
api = Api(app)


from resources import TextResource
from app.views import index


api.add_resource(TextResource, '/api/text')
