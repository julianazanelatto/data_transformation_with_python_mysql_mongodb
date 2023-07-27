# type:ignore
from sqlalchemy import create_engine


class MySQLConnection:
    def __init__(self, user, pwd=None, host='Localhost', port=3306,
                 database=None) -> None:
        """
            Initializing connection with MySQL database
            :param user: databse user
            :param pwd: password to access
            :param host: localhost, ip or domain
            :param port: port default 3306
            :param database: name of database to access
        """

        self.user = user
        self.pwd = pwd
        self.host = host
        self.port = port
        self.database = database
        self.engine = None

    def set_mysql_engine(self):
        """
            Create a engine to SQL queries and connect it.
            :return: engine connected to MySQL server
        """
        connection_string = ''.join(['mysql+pymysql://', self.user, ':',
                                    self.pwd, '@', self.host, ':',
                                    str(self.port), '/', self.database])

        self.database = create_engine(connection_string)
        try:
            self.engine = self.database.connect()
        except ConnectionError:
            raise 'Error during the connection'


QUERY = "SELECT o.orderNumber AS 'id_order', \
                c.customerNumber AS 'id_customer',\
                o.orderDate AS 'order_date',\
                o.status,\
                p.productCode AS 'id_product', \
                p.productName AS 'name',\
                p.productLine AS 'category',\
                od.quantityOrdered AS 'quantity',\
                od.priceEach AS 'price',\
                c.city,\
                c.state,\
                c.country\
            FROM orders o\
                INNER JOIN orderdetails od ON o.orderNumber = od.orderNumber\
                INNER  JOIN products p ON od.productCode = p.productCode\
                INNER JOIN customers c ON c.customerNumber = o.customerNumber\
            ORDER BY o.orderNumber;"
