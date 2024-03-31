##THIS IS CODE IS ONLY TO BE RUN ONCE FOR THE FIRST USE OF THE ##PROJECT. AFTER THAT
##IT SHOULD ONLY BE USED IN CASE THE 'library.db' FILE GETS DELETED.


import sqlite3
conn = sqlite3.connect('library.db')
cur = conn.cursor()
cur.execute('CREATE TABLE books(bname varchar(50), code varchar(20), author varchar(30), price varchar(10))')
cur.execute('CREATE TABLE log(pname varchar(30), phno varchar(11), class varchar(5), membno varchar(15), bname varchar(50), task varchar(10), day varchar(11))')
cur.execute('CREATE TABLE dues(pname varchar(30),bname vachar(50), membno varchar(15))')
cur.execute('CREATE TABLE stud(pname varchar(30), phno varchar(11), membno varchar(15), class varchar(5))')

#==========================ADDING VALUES============================

t=('Computer Science With Python','ISBN 945621448','Sumit Arora','400')
cur.execute('INSERT INTO books VALUES(?,?,?,?)',t)

t=('Concept Of Physics Vol.I','ISBN 9456325144','H.C. Verma','350')
cur.execute('INSERT INTO books VALUES(?,?,?,?)',t)

t=('Concept Of Physics Vol.II','ISBN 9456324431','H.C. Verma','350')
cur.execute('INSERT INTO books VALUES(?,?,?,?)',t)

t=('Aniket','8420427577','02832020','XII')
cur.execute('INSERT INTO stud VALUES(?,?,?,?)',t)

t=('Rohit','94563XXXXX','02752020','XII')
cur.execute('INSERT INTO stud VALUES(?,?,?,?)',t)

t=('Rana','98624XXXXX','03472020','XII')
cur.execute('INSERT INTO stud VALUES(?,?,?,?)',t)

t=('Aryan','98956XXXXX','45472020','XII')
cur.execute('INSERT INTO stud VALUES(?,?,?,?)',t)

conn.commit()
