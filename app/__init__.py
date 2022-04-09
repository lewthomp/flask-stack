import os
from flask import Flask, g, current_app
from flask_pymongo import PyMongo
from . import db


def create_app(test_config=None):
    """
    Application factory function.
    Creates Flask instance, sets default configuration, leaving room for 
    overriding.
    Ensures instance path exists to contain SQLite database.
    Creates simple /hello route to test application.
    Bash:
    $ export FLASK_APP=app
    $ export FLASK_ENV=development
    $ flask run
    """
    print("\n** Initialising app\n")
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")
    app.config["MONGO_URI"] = "mongodb://localhost:27017/demo"
    db.init_app(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    print("* Flask app object:", type(app), app)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/test')
    def hello():
        print(g.db)
        return "Hello cunts!"
    

    return app
