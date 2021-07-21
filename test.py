import pymysql


conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
cursor = conn.cursor()
cursor.execute("delete from user where name='류선영'")
