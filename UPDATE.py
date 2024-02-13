import sqlite3

conn = sqlite3.connect("test.db")
print("Opened successfully")
#HOW TO CHANGE VALUES
conn.execute("UPDATE EMPLOYEE6 SET AGE =54 WHERE ID=44 ")
conn.commit()


cursor = conn. execute("SELECT ID, NAME , AGE, SALARY FROM EMPLOYEE6")

for row in cursor:
    print("ID", row[0])
    print("NAME", row[1])
    print("AGE", row[2])
    print("SALARY", row[3])

print("Records found")
conn.close()