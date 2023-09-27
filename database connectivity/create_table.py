import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="sreelekha",password="Siri@1234",database="db2")
table="""
create table employee(
eid int,
ename varchar(32)
esal int
);
"""
mycursor=mydb.cursor()
mycursor.execute(table)
mydb.commit()
mycursor.close()
mydb.close()
