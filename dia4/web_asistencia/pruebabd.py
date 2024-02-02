import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='asistencia'
)

cursor = conn.cursor()
cursor.execute('select * from alumno')
data = cursor.fetchall()
print(data)
cursor.close()