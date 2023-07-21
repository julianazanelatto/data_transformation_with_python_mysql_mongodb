from Extract.mysql_connection import MySQLConnection
from Load.mongodb_connection import MongoDBConnection
from sqlalchemy import text
from Tranformation.data_transformation import transformig_data
from Extract.mysql_connection import QUERY

if __name__ == '__main__':

    # ----------- Step 1 (Extract): Connecting and retrieving the data ------------

    instance_mysql = MySQLConnection(user='root',
                                     passwd='mknj0912!',
                                     database='classicmodels')
    instance_mysql.set_mysql_engine()
    engine = instance_mysql.engine

    sql_query = text(QUERY)
    query_result = engine.execute(sql_query) # .fetchall() #l ista de tuplas

    # ----------- Step 2 (Transform): Data Transformation -------------

    posts = transformig_data(data = query_result.mappings().all()) # sending a dict
    print('Total de docs:',len(posts))

    # ----------- Step 3 (Load): Connection and data insertion into MongoDB -----------

    instance_mongodb = MongoDBConnection(domain='cluster0.2nj1fc2.mongodb.net/?retryWrites=true&w=majority',
                                          user='pymongo',
                                          passwd='o8ZkWJedxOywwtt4')

    client = instance_mongodb.connecting()
    # db = client['dio_analytics']
    db = client.get_database('dio_analytics')  # if doesn't exists will be created

    print('Coleções:\n',db.list_collection_names())
    # posts_collection = db.get_collection('orders').find()

    collection = db.get_collection('orders')
    for doc in posts:
        result = collection.insert_one(doc)
        print(result.inserted_id)



