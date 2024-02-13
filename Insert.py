import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE6 VALUES  (41, 'FEITH KARIMI', 34,450000.00)")
conn.execute("INSERT INTO EMPLOYEE6 VALUES  (42, 'FELIX', 24,460000.00)")
conn.execute("INSERT INTO EMPLOYEE6 VALUES  (43, 'EDITH WAMBUI', 44,430000.00)")
conn.execute("INSERT INTO EMPLOYEE6 VALUES (44, 'IDRIS CHILANGO', 43,550000.00)")
conn.execute("INSERT INTO EMPLOYEE6 VALUES (45, 'SAHSA UMOER', 28,400000.00)")


conn.commit()
print("Records inserted successfully")
conn.close()




