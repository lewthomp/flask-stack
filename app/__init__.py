import os
from flask import Flask, g
from flask_pymongo import PyMongo
from . import auth


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )
    app.config["MONGO_URI"] = "mongodb://localhost:27017/demo"
    mongo = PyMongo(app)
    # set flask database
    g.db = mongo.db
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.bp)

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        post = mongo.db.posts.find_one()
        print(post)
        return f"{post}"

    return app
