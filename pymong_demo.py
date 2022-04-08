import pymongo


print("\n** PyMongo database demo running\n")

client = pymongo.MongoClient("mongodb://localhost:27017/demo")
db = client["demo"]

# print("List of databases")
# print(client.list_database_names())

postsCol = db["posts"]

post0 = {
    "_id": 0,
    "title:": "The Promised Land",
    "author": "rvdemonk",
    "tags": ['neoblog', 'blockchain', 'philosophy']    
}

def add_post(post: dict):
    return postsCol.insert_one(post)





