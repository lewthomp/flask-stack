import pymongo
import json

# import ipython


print("\n** PyMongo database demo running\n")

client = pymongo.MongoClient("mongodb://localhost:27017/demo")
db = client["demo"]

# print("List of databases")
# print(client.list_database_names())

postsCol = db["posts"]


def add_post(post: dict):
    return postsCol.insert_one(post)


def get_posts():
    return postsCol.find()


def main():
    collection = postsCol.find()
    for i, doc in enumerate(collection):
        print(f"{i}/", doc["_id"], doc["author"], doc["tags"])


if __name__ == "__main__":
    app = main()
