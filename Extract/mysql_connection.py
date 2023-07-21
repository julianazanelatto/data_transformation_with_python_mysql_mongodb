from sqlalchemy import create_engine


class MySQLConnection:
    def __init__(self, user, passwd = None, host = 'localhost' , port=3306, database=None):
        """
                Inicializando a classe de conexão ao banco de dados MySQL
            :param user: usuário do banco de dados
            :param passwd: senha caso exista
            :param host: localhost, ip ou domínio de destino
            :param port: porta default 3306
            :param database: banco de dados a ser acessado
        """
        self.user = user
        self.passwd = passwd
        self.database = database
        self.host = host
        self.port = port
        self.engine = None



    def set_mysql_engine(self):

        connection_string = ''.join(['mysql+pymysql://', self.user, ':', self.passwd, '@',
                                     self.host, ':', str(self.port), '/', self.database])
        # 'mysql://user:password@host:port/database'
        self.engine = create_engine(connection_string)
        try:
            self.engine.connect()
        except ConnectionError():
            raise 'Error during the connection'
    """
        Estabelecendo métodos de consulta:
        
        1 - Listagem das tabelas
        2 - Escolha de tabela
        3 - Execução de consulta a uma tabela
        4 - Junção entre tabelas
    """

# Funções de apoio


QUERY = query = (
        "SELECT o.orderNumber AS 'id_order', \
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
            ORDER BY o.orderNumber;"\
    )