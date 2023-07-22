"""
    This project is related to a ETL processing. The goal in here is collect the data from a
    RDBMs
"""
from sqlalchemy import text
from Extract.mysql_connection import MySQLConnection, QUERY
from Load.mongodb_connection import MongoDBConnection
from Tranformation.data_transformation import transforming_data

if __name__ == '__main__':

    # ----------- Step 1 (Extract): Connecting and retrieving the data ------------

    instance_mysql = MySQLConnection(user='root',
                                     passwd='senha',
                                     database='classicmodels')
    instance_mysql.set_mysql_engine()
    engine = instance_mysql.engine

    sql_query = text(QUERY)
    query_result = engine.execute(sql_query) # .fetchall() #l ista de tuplas3

    print("Closing the MySQL connection!")
    engine.dispose()

    # ----------- Step 2 (Transform): Data Transformation -------------

    posts = transforming_data(data = query_result.mappings().all()) # sending a dict
    print('Total de docs:',len(posts))

    # ------ Step 3 (Load): Connection and data insertion into MongoDB ---

    instance_mongodb = MongoDBConnection(
                            domain='cluster0.2nj1fc2.mongodb.net/?retryWrites=true&w=majority',
                            user='pymongo',
                            passwd='chave'
                        )

    client = instance_mongodb.connecting()
    # db = client['dio_analytics']
    db = client.get_database('dio_analytics')
    print('Coleções:\n',db.list_collection_names())

    collection = db.get_collection('orders')
    for doc in posts:
        result = collection.insert_one(doc)
        print(result.inserted_id)

    print("Closing the MongoDB connection!")
    client.close()
