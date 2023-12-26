import sqlite3
import hashlib
Dbconnect=sqlite3.connect("userdata.db")
cur=Dbconnect.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
     id INTEGER PRIMARY KEY,
     username VARCHAR(255) NOT NULL,
     password VARCHAR(255) NOT NULL      
)  
""")
username1,password1="abbas88",hashlib.sha256("202105138".encode('utf-8')).hexdigest()
username2,password2="mahmood77",hashlib.sha256("202106345".encode('utf-8')).hexdigest()
username3,password3="mohamedAlmeer",hashlib.sha256("ITNE352".encode('utf-8')).hexdigest()
cur.execute("INSERT INTO userdata(username,password)VALUES(?,?)",(username1,password1))
cur.execute("INSERT INTO userdata(username,password)VALUES(?,?)",(username2,password2))
cur.execute("INSERT INTO userdata(username,password)VALUES(?,?)",(username3,password3))
Dbconnect.commit()