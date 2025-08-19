import mysql.connector
 
 
# Connecting from the server
print("jii")
conn = mysql.connector.connect(user = 'root',host = 'localhost',
                               password="",
                              database = 'feedback_system')
 
print(conn,"hii")
 
# Disconnecting from the server
conn.close()