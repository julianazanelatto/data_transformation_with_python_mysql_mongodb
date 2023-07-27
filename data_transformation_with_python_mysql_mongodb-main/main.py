"""
    This project is related to a ETL processing. The goal in here is collect the data from a
    RDBMs
"""
# type:ignore

import os
import pprint

import dotenv
from sqlalchemy import text
from Transform.data_transformation import transforming_data

from Extract.mysql_connection import QUERY, MySQLConnection
from Load.mongodb_connection import MongoDBConnection

dotenv.load_dotenv()

if __name__ == '__main__':
    # ----------/ Step 1 (Extract): Connecting and retrieving the data /------
    instance_mysql = MySQLConnection(
        user=os.environ['MYSQL_USER'],
        pwd=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE']
    )

    engine = instance_mysql.set_mysql_engine()

    sql_query = text(QUERY)

    result = instance_mysql.engine.execute(sql_query)

    instance_mysql.database.dispose()

    # ----------/ Step 2 (Transform): Data Transformation /------------
    posts = transforming_data(result.mappings().all())  # sending a dict
    # print('Total de docs:', len(posts))

    # ----/ Step 3 (Load): Connection and data insertion into MongoDB /--
    instance_mongodb = MongoDBConnection(
        user=os.environ['MONGODB_USER'],
        pwd=os.environ['MONGODB_PASSWORD'],
        domain=os.environ['MONGODB_DOMAIN']
    )

    client = instance_mongodb.set_mongodb_connection()

    db, collection, posts_id = instance_mongodb.inserting_data_posts(
        db_name='dio_analytics',
        collection_name='orders',
        posts=posts[3:5])
    post_inserted = db.orders
    for id in posts_id:
        pprint.pprint(post_inserted.find_one({'_id': id}))
