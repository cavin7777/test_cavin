import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

db = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="cavin",
    db="CAVIN"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM users;")
for row in cursor.fetchall():
    print(row)

db.close()
