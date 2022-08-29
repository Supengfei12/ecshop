import pymysql


class ECSHOPDB:
    def __init__(self):
        self.db = pymysql.connect(
            user='su',
            password='',
            host='192.168.88.102',
            database='ecshop',
            port=3306,
            charset='utf8'
        )
    def delete_data(self,table_name,column_name,value):
        sql = 'delete from {} where {} = "{}";'.format(table_name,column_name,value)
        cur = self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        self.db.close()


if __name__ == '__main__':
    ECSHOPDB().delete_data('users','user_name','李克强')
