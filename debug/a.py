import pymysql

db = pymysql.connect(
    user='root',
    password='',
    host='192.168.88.101',
    database='ecshop',
    port=3306,
    charset='utf8'
)

cur = db.cursor()
sql = "select * from users;"
cur.execute(sql)
data = cur.fetchmany(3)
print(data)
db.commit()
db.close()
