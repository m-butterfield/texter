from flask import Flask
from flask.ext.restful import Api


app = Flask(__name__)
api = Api(app)


from resources import TextResource
from demo_site.views import index


api.add_resource(TextResource, '/api/text')
