
import os
# mysql+pymysql://root:root@127.0.0.1:3306/db_demo1
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlktqa_demo'

DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,

                                                                    HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
SECRET_KEY ='123'
#b'\x1e\xe5\x8c4\xdb_+\xd4\xec\xbd'
