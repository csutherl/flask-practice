import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb
import json

class DB_Connector():

    def __init__(self):
        self.db_conn = MySQLdb.connect(host="localhost", # your host, usually localhost
            user="py", # your username
            passwd="py_pass", # your password
            db="testing", # name of the data base
            use_unicode=True)

        # you must create a Cursor object. It will let
        #  you execute all the query you need
        self.cur = self.db_conn.cursor(MySQLdb.cursors.DictCursor)

    def getAll(self):
        # Use all the SQL you like
        self.cur.execute("SELECT * FROM proc_status")

        # the cls arg allows me to use my custom encoder that allows me to encode datetimes
        json_row = json.dumps(self.cur.fetchall(), cls=CustomEncoder)
        return json_row

# Who can't jsonify datetimes :P
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime):
            # is iso format ok, or do we want something different?
            return obj.isoformat()
        return json.JSONEncoder.default(self,obj)
