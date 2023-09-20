import pymysql


def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='pythondb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


connectdb()

print(connectdb())
