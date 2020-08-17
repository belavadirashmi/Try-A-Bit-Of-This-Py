import sys,csv,time,pyodbc
import pandas as pn

cnxserver="Driver={SQL Server Native Client 11.0};" "Server=LAPTOP-1PE9K4I8\\SQLEXPRESS;" "Database=Dev;" "Trusted_Connection=yes;" 
cnx=pyodbc.connect(cnxserver)
mycursor=cnx.cursor()
csql="IF OBJECT_ID('dbo.Enrolments', 'U') IS NULL create table dbo.Enrolments (Date date,Year integer,Semester integer,Course char(5),Name varchar(50),Country varchar(40),VisaStatus varchar(25))"
mycursor.execute(csql)
cnx.commit()
mycursor.execute("select * from INFORMATION_SCHEMA.TABLES")
for tab in mycursor:
	print(tab)

rdf=pn.read_csv("D:\\Cloud\\MoreGyanPlease\\EnrolmentTxn_Aug1.csv",delimiter=",")

for index, rec in rdf.iterrows():
	print (rec)
	mycursor.execute("INSERT INTO dbo.Enrolments(Date,Year,Semester,Course,Name,Country,VisaStatus) values(?,?,?,?,?,?,?)",
		rec['Date'],rec['Year'],rec['Semester'],rec['Course'],rec['Name'],rec['Country'],rec['VisaStatus'])
	cnx.commit()
