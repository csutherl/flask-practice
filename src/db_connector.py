import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb
import json

class DB_Connector():

    def __init__(self):
        self.db_conn = MySQLdb.connect(host="localhost", # your host, usually localhost
            user="py", # your username
            passwd="py_pass", # your password
            db="test", # name of the data base
            use_unicode=True)

        # you must create a Cursor object. It will let
        #  you execute all the query you need
        self.cur = self.db_conn.cursor(MySQLdb.cursors.DictCursor)

    def getAll(self):
        # Use all the SQL you like
        self.cur.execute("SELECT * FROM test")

        json_row = json.dumps(self.cur.fetchall())
        return json_row
