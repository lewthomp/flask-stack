import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_pymongo import PyMongo


def get_db():
    if 'db' not in g:
        pass
    # connect to db
    return


def close_db(e=None):
    d= g.pop('db', None)
    if db is not None:
        db.close()