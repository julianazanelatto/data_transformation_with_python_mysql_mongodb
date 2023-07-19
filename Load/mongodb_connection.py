import pymongo
from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self, domain='localhost', user='pymongo', passwd=None):
        self.host = domain
        self.user = user
        self.passwd = passwd

    def connecting(self):
        # mongodb+srv://pymongo:<password>@cluster0.2nj1fc2.mongodb.net/?retryWrites=true&w=majority
        connection_string = ''.join(['mongodb+srv://',self.user,':',self.passwd,'@',self.host])
        return MongoClient(connection_string)



