import pymysql; 
pymysql.install_as_MySQLdb();

import MySQLdb

db_conn = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="py", # your username
                     passwd="py_pass", # your password
                     db="test", # name of the data base
                     use_unicode=True)

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db_conn.cursor(MySQLdb.cursors.DictCursor) 

# Use all the SQL you like
cur.execute("SELECT * FROM test")

row = cur.fetchall()

# print all the first cell of all the rows
#for row in cur.fetchall() :
#    print str(row[0]) + " " + str(row[1])
