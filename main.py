from Extract.connecting_mysql import MySQLConnection
from Load.connecting_mongodb import MongoDBConnection
from sqlalchemy import inspect

if __name__ == '__main__':

    instance_mysql = MySQLConnection(user='root',
                                     passwd='mknj0912!',
                                     database='employees')
    instance_mysql.set_mysql_engine()
    inspector_engine = inspect(instance_mysql.engine)

    # connecting to the mongodb

    # mongodb+srv://pymongo:<password>@
    instance_mongodob = MongoDBConnection(domain='cluster0.2nj1fc2.mongodb.net/?retryWrites=true&w=majority',
                                          user='pymongo',
                                          passwd='o8ZkWJedxOywwtt4')

    conn = instance_mongodob.client().db