from Extract.mysql_connection import MySQLConnection
from Load.mongodb_connection import MongoDBConnection
from sqlalchemy import inspect, text
from Tranformation.documents_creation import transformig_data, inserting_data_posts

if __name__ == '__main__':

    instance_mysql = MySQLConnection(user='root',
                                     passwd='mknj0912!',
                                     database='classicmodels')
    instance_mysql.set_mysql_engine()
    engine = instance_mysql.engine

    query = (
        "SELECT o.orderNumber AS 'id_order', \
                c.customerNumber AS 'id_customer',\
                o.orderDate AS 'order_date',\
                o.status,\
                p.productCode AS 'Id_product', \
                p.productName AS 'Name',\
                p.productLine AS 'Category',\
                od.quantityOrdered AS 'quantity',\
                od.priceEach AS 'price',\
                c.city,\
                c.state,\
                c.country\
            FROM orders o\
                INNER JOIN orderdetails od ON o.orderNumber = od.orderNumber\
                INNER  JOIN products p ON od.productCode = p.productCode\
                INNER JOIN customers c ON c.customerNumber = o.customerNumber\
            ORDER BY o.orderNumber;"\
    )
    sql_query = text(query)
    result = engine.execute(sql_query) # .fetchall() #lista de tuplas

    #starts the transformation
    posts = transformig_data(data= result.mappings().all()) #sending a dict
    # inserting_data_posts(posts)




