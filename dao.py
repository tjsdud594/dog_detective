import pymysql
import collections
import json


class Database2():
    def insertdb(data):
    # def insertdb():
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
            cursor = conn.cursor()

            try:
                cursor.execute("INSERT INTO user(id, pw, name, email) VALUES (%s, %s, %s, %s)", data)
                # cursor.execute("INSERT INTO user(id, pw, name, email) VALUES ('tjsdud594', '1234@', '룬선영', 'fbtjsdud594@gmail.com')")
            except Exception as e:
                print(e)
            
        except Exception as e:
            print(e)

        conn.commit()
        conn.close()


    def email_check(email):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
            cursor = conn.cursor()

            try:
                cursor.execute("SELECT * FROM USER WHERE email=%s", email)
                row = cursor.fetchone()
                print(row)
                return row
            except Exception as e:
                print(e)
            
        except Exception as e:
            print(e)

        conn.commit()
        conn.close()

    def id_check(id):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
            cursor = conn.cursor()

            try:
                cursor.execute("SELECT * FROM USER WHERE id=%s", id)
                row = cursor.fetchone()
                print(row)
                return row
            except Exception as e:
                print(e)
            
        except Exception as e:
            print(e)

        conn.commit()
        conn.close()



    def deletedb(id):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
            cursor = conn.cursor()

            try:
                cursor.execute("delete from user where email=(select sub_user.email from ( select email from user where id=%s) sub_user)", id)
                print('완료')
            except Exception as e:
                print(e)
            
        except Exception as e:
            print(e)

        conn.commit()
        conn.close()


    def selectdb():
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
            cursor = conn.cursor()
            try:
                cursor.execute("select * from user")
                rows = cursor.fetchall()
                print(rows)

            except Exception as e:
                print(e)
            
        except Exception as e:
            print(e)
        
        conn.commit()
        conn.close()



    def logindb(idpw):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
            cursor = conn.cursor()
            
            try:
                cursor.execute("select * from user where id=%s and pw = %s", idpw)
                row = cursor.fetchone()
                print(row)
                return row

            except Exception as e:
                print(e)
            
        except Exception as e:
            print(e)
                
        conn.commit()
        conn.close()

    def insert(data):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO product(p_name, p_price) VALUES (%s, %s)", data)
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        conn.commit()
        conn.close()

    def select(data):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM user where id = %s", data)
                rows = cursor.fetchall()
                v = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['name'] = row[3]
                    d['id'] = row[1]
                    d['email'] = row[4]
                    v.append(d)
                data = json.dumps(v, ensure_ascii=False)
                print(data)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return data
        # print(data)


    def insertdb2(data):
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO p_order(p_name, p_price, id) VALUES (%s, %s, %s)", data)
            print('DB 완료')

        except Exception as e:
            print(e)
        
        conn.commit()
        conn.close()


    def view_order(id):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
            cursor = conn.cursor()

            try:
                cursor.execute("select * from p_order where id=%s", id)
                rows = cursor.fetchall()
                v = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['p_no'] = row[0]
                    d['p_name'] = row[1]
                    d['p_price'] = row[2]
                    d['id'] = row[3]
                    v.append(d)
                data = json.dumps(v, ensure_ascii=False)
                print(data)

                print('완료')
            except Exception as e:
                print(e)
            
        except Exception as e:
            print(e)

        conn.commit()
        conn.close()
        return data


# if __name__=="__main__":
#     # -*- conding: utf-8 -*-
    # Database2.deletedb()
    # Database2.insertdb()
    # Database2.selectdb()
    # Database2.email_check('ddd@naver.com')