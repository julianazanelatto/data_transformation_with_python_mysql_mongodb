import pprint

from Load.mongodb_connection import MongoDBConnection

# connecting to the mongodb

# mongodb+srv://pymongo:<password>@
instance_mongodob = MongoDBConnection(domain='cluster0.2nj1fc2.mongodb.net/?retryWrites=true&w=majority',
                                      user='pymongo',
                                      passwd='o8ZkWJedxOywwtt4')

client = instance_mongodob.connecting()
db = client.get_database('dio_analytics') # if doesn't exists will be created
posts = db.get_collection('orders')
print(posts)

# collection = db.get_collection(posts[0])
# for element in collection.find():
#    print(element)