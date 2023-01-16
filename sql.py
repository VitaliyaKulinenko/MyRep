import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password="bezhok1994",
    db='students',
)

cur = conn.cursor()
cur.execute("select * from list")
output = cur.fetchall()
print(output)

conn.close()

# INSERT INTO 'LIST' ('id', 'name','surname','course') VALUES ('10','ИВАН', 'ПЕТРОВ', '5')
a_students = []
a_students.append (input("id"))
a_students.append (input("name"))
a_students.append (input("surname"))
a_students.append (input("course"))
cur.execute("INSERT INTO 'LIST' ('id', 'name','surname','course') VALUES ('10','ИВАН', 'ПЕТРОВ', '5')")%tu




