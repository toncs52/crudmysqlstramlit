import pymysql


def connectdb():
    connection = pymysql.connect(
        host='b1wpwa3shylejnjwbjo9-mysql.services.clever-cloud.com',
        user='u7qvkmr7apowq5mt',
        password='hs4xjnz9HT67WTFro8Uc',
        db='b1wpwa3shylejnjwbjo9',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


connectdb()

print(connectdb())
