import pymongo
from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, domain='localhost', user='pymongo', passwd=None):
        self.domain = domain
        self.user = user
        self.passwd = passwd
        self.client = None

    def connecting(self):
        # mongodb+srv://pymongo:<password>@cluster0.2nj1fc2.mongodb.net/?retryWrites=true&w=majority
        connection_string = ''.join(['mongodb+srv://',self.user,':',self.passwd,'@',self.domain])
        return MongoClient(connection_string)

def inserting_data_posts(db, posts, collection_name: str):
    collection = db.client.get_collection(collection_name)
    print(type(posts))
    if type(posts) is dict:
        post_id = collection.insert_one(posts).inserted_id
    else:
        result = collection.insert_many(posts)
    return result.inserted_ids
