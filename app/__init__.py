import os
<<<<<<< HEAD
from flask import Flask, g, current_app
from flask_pymongo import PyMongo


def create_app(test_config=None):
    """
    Application factory function.
    Creates Flask instance, sets default configuration, leaving room for 
    overriding.
    Ensures instance path exists to contain SQLite database.
    Creates simple /hello route to test application.

    Bash:
    $ export FLASK_APP=flaskr
    $ export FLASK_ENV=development
    $ flask run
    """
    print("\n** Initialising app\n")
=======
from flask import Flask, g
from flask_pymongo import PyMongo
from . import auth


def create_app(test_config=None):
>>>>>>> 5a01c2fa7926e3d7bf8c9fce66cf680ad373c8e2
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )
<<<<<<< HEAD
    app.config["MONGO_URI"] = "mongodb://localhost:27017/"
    
    # databse stuff
    mongo = PyMongo(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
=======
    app.config["MONGO_URI"] = "mongodb://localhost:27017/demo"
    mongo = PyMongo(app)
    # set flask database
    g.db = mongo.db
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
>>>>>>> 5a01c2fa7926e3d7bf8c9fce66cf680ad373c8e2
    else:
        app.config.from_mapping(test_config)

<<<<<<< HEAD
    print("* Flask app object:", type(app), app)
    # print("* Flask current_app object:", type(current_app), current_app)
    # print("* Are these equivalent?", (app == current_app))

    #ensure the instance folder exists
=======
    # ensure the instance folder exists
>>>>>>> 5a01c2fa7926e3d7bf8c9fce66cf680ad373c8e2
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

<<<<<<< HEAD
    #a simple page that says hello
    @app.route('/test')
    def hello():
        return "Hello cunts!"
    
    return app
=======
    app.register_blueprint(auth.bp)

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        post = mongo.db.posts.find_one()
        print(post)
        return f"{post}"

    return app
>>>>>>> 5a01c2fa7926e3d7bf8c9fce66cf680ad373c8e2
