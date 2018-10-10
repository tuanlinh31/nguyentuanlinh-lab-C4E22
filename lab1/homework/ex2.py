from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database()

posts = db["posts"]

post = {
    "title": "Hom nay troi dep",
    "content": "Toi di choi ",
    "author": "Linh"
}

posts.insert_one(post)
