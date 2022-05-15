import pyodbc

# ms_driver=[x for x in pyodbc.drivers() if "ACCESS" in x.upper()]
# print(f"MS-Access Driver : {ms_driver}")

try:
    conne=r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\vikram\\Documents\\test.accdb;'
    conn= pyodbc.connect(conne)
    #print("Connected")
except pyodbc.Error as e:
    print("Error in Connection", e)

cursor=conn.cursor()

# INSERT DATA
# cursor.execute('INSERT INTO users (name, email, mobile) VALUES (?,?,?)',("test","test12@gmail.com",123))
# conn.commit()
# print("success")

# Data fetch
# data=cursor.execute('SELECT * FROM users')
# for row in data.fetchall():
#     print(row)

# DATA update
# name="vk"
# id=9
# cursor.execute("UPDATE users SET name=? WHERE ID =?",(name, id))
# conn.commit()
# print("Data Updated")

# Data delete
id=6
cursor.execute("DELETE FROM users WHERE ID=?",(id))
conn.commit()
print("DELETED")