import mysql.connector

# Connect to MySQL
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="joshimysqlsam*03",
        database="careerswebsite"
    )
    return conn

print("Connection successful!")

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM jobs")
# rows = cursor.fetchall()
#
# columns = [desc[0] for desc in cursor.description]
#
# for row in rows:
#     #print(row)
#     # print(type(row))  # shows the type of 'row'
#     # print(type(row[0]))
#     for col_name, value in zip(columns, row):
#         print(f"{col_name}: {value}")
#
#
#
#
# cursor.close()
# conn.close()
