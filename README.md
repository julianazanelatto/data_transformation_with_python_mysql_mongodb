  # Data Transformation With Python Mysql Mongodb Database

## Project: RDBMS to MongoDB Data Transformation

This repository is related to a data ETL for DIO class called acelleration. In this particular class, we going to build a code with three steps: Step 1: collect data from MySQL; Step 2: transforma the data; Step 3: Ingest the data into the new model with MongoDB Database.

To understand more about Relational and NoSQL databases, you can access the following links:
1. [SQL or NoSQL - Portuguese youtube video](https://youtu.be/o8i2KZiIW4Y)
3. [Youtube Playlist about databases](https://youtube.com/playlist?list=PLigQ9zMmlIqK38m2kShipMoquEcasoWKZ)
4. [SQL from scratch - Youtube Playlist in progress](https://youtube.com/playlist?list=PLigQ9zMmlIqIc2xi1Sg902zCscNndIvDp)
5. [Tutorials in my site - SR](https://simplificandoredes.com/)

For this particular project we gonna use a sample of mysqlututorial.org named as classicmodels. You can download this sample from [here](https://www.mysqltutorial.org/mysql-sample-database.aspx) or from this repository. With this samples in hands, you will restore the database using the follow command:

  > mysql -u <user> -p -t < mysqlsampledatabase.sql

Therefore, you will be able to query the data using SQL.

OK, kepping going ... In the following steps we gonna understand the purpose of this project.

Some of the prerequisites are:
1. MySQL local installed or an instance on cloud
2. MongoDB local installed or an instance on cloud
3. Python 3.10 installed

### Project scenario:

For this project I have a MySQL sever 8.0 installed on my ubuntu machine. However, for the NoSQL step I used the MongoDB Database on MongoDB Atlas. Therefore, the code will reflect the configurations accordingly to the previus definition. An IDE can be of your choose, I particulary enjoy the Pycharm IDE.


## ETL Processing - Extract Step

### Step 1: Set up the Environment

Ensure you have the required libraries installed. You can install them using pip:

    pip install SQLAlchemy pymongo pandas

(or polars if you choose to use it instead of pandas)

If you don't have the connector run the follow command:

    > pip install pymysql

In this particular project we gonna use the [PyMySQL](https://pypi.org/project/pymysql/) driver.However there are others that you can use. Feel free to modify for a driver of your own choose.

### Step 2: Connect to MySQL Database

Use SQLAlchemy to connect to your MySQL database and fetch the data you want to transform. Replace the placeholders in the code below with your actual database connection details:

    # Connection String used 
    # Replace 'mysql+pymysql://user:password@host:port/database' with your MySQL connection string

Bellow you gonna find the connection method that is related to the MySQLConnection class in the code. You will find this piece of code into the mysql_connection.py. 

    from sqlalchemy import create_engine
    def set_mysql_engine(self):

    connection_string = ''.join(['mysql+pymysql://', self.user, ':', self.passwd, '@',
                                 self.host, ':', str(self.port), '/', self.database])
    # 'mysql://user:password@host:port/database'
    self.engine = create_engine(connection_string)
    try:
        self.engine.connect()
    except ConnectionError():
        raise 'Error during the connection'

## ETL Processing - Transformation Step

### Step 3: Data Transformation and Modeling

Perform any necessary data transformation using pandas or polars (depending on your choice). This might include cleaning, filtering, aggregating, or any other manipulation required to prepare the data for MongoDB insertion.

    def transforming_data(data):
    """
        Transformation of the data from tabular to document format
    :param data: dict with the tabular data
    :return: dict based in json document format

      1° step: receive the data and convert into a dataframe
      2° step: retrive the dataframe subset based on the context data
      3° step: build the new model - document oriented
    
    """

### Step 4: Connect to MongoDB

Use PyMongo to establish a connection to your MongoDB server. Replace the placeholders in the code below with your MongoDB connection details:

    from pymongo import MongoClient

    # Replace 'mongodb://user:password@host:port/' with your MongoDB connection string
    client = MongoClient('mongodb://user:password@host:port/')
    db = client['your_database_name']  # Replace 'your_database_name' with your desired database name
    collection = db['your_collection_name']  # Replace 'your_collection_name' with your desired collection name

To be able to connect to the MongoDB Database on Atlas you need to install another package: "pymongo[srv]"

    > python3.10 -m pip install "pymongo[srv]"


### Step 5: Data Ingestion into MongoDB

Iterate over the transformed data and insert it into MongoDB:

    # Assuming your transformed data is stored in the 'data' DataFrame
    for index, row in data.iterrows():
        document = row.to_dict()
        collection.insert_one(document)

### Step 6: Complete the Script

Put everything together into a Python script, and you have your data engineering project ready to go. You can run the script whenever you need to transfer data from MySQL to MongoDB.

Remember to handle any potential errors, add logging, and optimize the code based on the scale of your data.

Please note that the provided steps are just a basic outline, and you can expand the project according to your specific requirements and the complexity of your data transformation needs. Happy coding!

Others sources:
- https://pymongo.readthedocs.io/en/stable/api/bson/index.html
- https://pymongo.readthedocs.io/en/stable/tutorial.html#
