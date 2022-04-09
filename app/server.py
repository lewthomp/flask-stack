import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/app"
app.config.from_mapping({"MONGO_URI": "mongodb://localhost:27017/app"})
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api")
def api():
    post = mongo.db.posts.find_one()
    return post
