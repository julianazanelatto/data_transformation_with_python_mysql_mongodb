import pymongo


class MongoDBConnection:
    def __init__(self, host='localhost'):
        self.host = host