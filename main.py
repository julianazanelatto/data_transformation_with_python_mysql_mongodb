from Extract.connecting_mysql import MySQLConnection
from sqlalchemy import inspect

if __name__ == '__main__':

    conn = MySQLConnection(user='root', passwd='mknj0912!', database='employees')
    conn.set_mysql_engine()
    inspector_engine = inspect(conn.engine)