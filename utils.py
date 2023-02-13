import mysql.connector as mariadb

db_host="localhost"
db_port="3306"
user="root"
password="123456"
db_name="itnm"

conn2 = mariadb.connect(host=db_host, port=db_port, user=user,
    password=password,
    database=db_name)

def reconnect():
    global conn2
    conn2 = mariadb.connect(host=db_host, port=db_port, user=user,
    password=password,
    database=db_name)
    return conn2    


# def executeSql(sql):
#     cur = conn2.cursor(dictionary=True)
#     #print(f"Executing: {sql}")
#     cur.execute(sql)
#     res = cur.rowcount
#     conn2.commit()
#     cur.close()

#     return res

# def querySql(sql):
#     cur = conn2.cursor(dictionary=True)
#     #print(f"Executing: {sql}")
#     cur.execute(sql)
#     res = cur.fetchall()
#     cur.close()

#     return res

    # cur = conn2.cursor(dictionary=True)
    # cur.execute("select * from inventory;")
    # res = cur.fetchall()
    # cur.close()
    # print(list(res))

async def getDevices():
    try:
        conn2 = reconnect()
        print("get lists from module...")
        cur = conn2.cursor(dictionary=True)
        sql = "select * from inventory;"
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        print("getlists from module done!!!")
        
        return list(res)
    except Exception as ex:
        reconnect()
        print(ex)
        return None

async def addDevice(name,ip):
    try:
        conn2 = reconnect()
        print("insert user")
        cur = conn2.cursor(dictionary=True)
        sql = 'INSERT INTO inventory (name,ip, status) VALUES ("'+name+'", "'+ip+'", "New");'
        print(sql)
        cur.execute(sql)
        # res = cur.fetchall()
        conn2.commit()
        print("user inserted")
        
        return list([])
    except Exception as ex:
        reconnect()
        print(ex)
        return None

async def editDevice(origin,name,ip):
    try:
        conn2 = reconnect()
        print("insert user")
        cur = conn2.cursor(dictionary=True)
        sql = 'UPDATE inventory SET name="'+name+'",ip="'+ip+'" WHERE ip="'+origin+'";'
        print(sql)
        cur.execute(sql)
        # res = cur.fetchall()
        conn2.commit()
        print("user inserted")
        
        return list([])
    except Exception as ex:
        reconnect()
        print(ex)
        return None

async def deleteDevice(name,ip):
    try:
        conn2 = reconnect()
        print("insert user")
        cur = conn2.cursor(dictionary=True)
        sql = 'DELETE FROM inventory WHERE ip="'+ip+'";'
        print(sql)
        cur.execute(sql)
        # res = cur.fetchall()
        conn2.commit()
        print("user inserted")
        
        return list([])
    except Exception as ex:
        reconnect()
        print(ex)
        return None






