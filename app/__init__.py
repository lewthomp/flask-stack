import os
from flask import Flask


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
    # create and configure app
    print("Name: ", __name__)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello cunts'
    
    return app