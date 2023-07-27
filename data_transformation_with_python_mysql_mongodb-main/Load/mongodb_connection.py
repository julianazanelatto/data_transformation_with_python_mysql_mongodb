# type:ignore
from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self, domain='localhost', user='pymongo', pwd=None) -> None:
        """
            Initializing connection with MongoDB database
            :param user: databse user
            :param pwd: password to access database
            :param domain: name of cluster to access cluster0.psuuo6q.mongodb
        """
        self.domain = domain
        self.user = user
        self.pwd = pwd
        self.client = None

    def set_mongodb_connection(self):
        """
            Create a client to CRUD a MongoDB database and connect it.
            mongodb+srv://hugommjunior:<password>@cluster0.psuuo6q.mongodb.net/?retryWrites=true&w=majority
        """

        connection_string = ''.join(
            ['mongodb+srv://', self.user, ':', self.pwd, '@', self.domain])
        return MongoClient(connection_string)

    def inserting_data_posts(self, db_name: str, collection_name: str, posts):
        """
            Function to insert into one or many data into MongoDB database
            :param db_name: name of database to create it if doesn't exists
            :param collection_name: name of collection where the data inserted
                    to and create it if doesn't exists
            :param posts: data formatted to insert into collection
            :return db, collection, posts_id: connections of db and collection
                    to use and a list of id posts to find them               
        """
        client = self.set_mongodb_connection()
        db = client.get_database(db_name)
        collection = db.get_collection(collection_name)
        posts_id = []
        for doc in posts:
            post_id = collection.insert_one(doc).inserted_id
            posts_id.append(post_id)
            print(post_id)

        return db, collection, posts_id
