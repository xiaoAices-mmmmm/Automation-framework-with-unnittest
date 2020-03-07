import pymysql
import os
from pymysql.err import DatabaseError
import configparser

# ======== Reading db_config.ini setting ===========
data_file_path = os.path.dirname(os.path.dirname(__file__))
base_dir = data_file_path.replace('\\','/')
file_path = base_dir + '/db_config.ini'
conf = configparser.ConfigParser()
conf.read(file_path,encoding='utf8')
host = conf.get('mysqlconf','host')
pot = conf.get('mysqlconf','port')
user = conf.get('mysqlconf','user')
password = conf.get('mysqlconf','password')
db_name = conf.get('mysqlconf','db_name')
char = conf.get('mysqlconf','char')

#链接数据库
class db:
    def __init__(self):
        try:
            self.connent = pymysql.connect(
                host = host,
                port = int(pot),
                db = db_name,
                user = user,
                password = password,
                charset = char,
            )
        except DatabaseError as e:
            print(r"no database{},{}".format(e.args[0],e.args[1]))

    def clear(self,table_name):#清理数据库
        clear_sql = "DELETE FROM " + table_name +' ;'
        with self.connent.cursor() as cursor:
            cursor.execute(clear_sql)
        self.connent.commit()

    def insert(self,table_name,insert_data):
        '''插入数据'''
        for key in insert_data:
            insert_data[key] = "'"+insert_data[key] + "'"
        key = ','.join(insert_data.keys())
        values = ','.join(insert_data.values())
        insert_sql = "INSERT INTO " + table_name + "(" + key +")" +' values ' + "(" + values +");"
        with self.connent.cursor() as cursor:
            cursor.execute(insert_sql)
        self.connent.commit()

    def close(self): #关闭数据库链接
        self.connent.close()

dbs = db()
data = {'Symbol':'BBP','Company':'BANNER LNC.','Industry':'Technology'}
dbs.insert('stocks',data)
dbs.close()
