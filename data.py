# coding:utf-8
from flask.ext.pymongo import PyMongo

db = None


def init(app):
    with app.app_context():
        mongo = PyMongo(app).db
    global db
    db = mongo
    return db
