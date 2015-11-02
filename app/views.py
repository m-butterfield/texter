"""
Views for the application

"""
from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return 'Not found :(', 404
