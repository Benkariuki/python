import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")


conn.execute("DELETE FROM EMPLOYEE6 WHERE ID=45")
conn.commit()

cursor = conn.execute("SELECT ID , NAME ,AGE, SALARY FROM EMPLOYEE6")

for row in cursor:
        print("ID", row[0])
        print("NAME", row[1])
        print("AGE", row[2])
        print("SALARY", row[3])
