# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:40:14 2018

@author: arpit
"""

#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('Ez_data.db')

print "Opened database successfull"

conn.execute('''CREATE TABLE RESTRAUNT
         (RES_ID INT PRIMARY KEY     NOT NULL,
         RES_NAME           TEXT    NOT NULL,
         RES_ph            INT     NOT NULL,
         ADDRESS        CHAR(50),
         RATING         INT);''')
print "Table created successfully";

conn.close()
conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute("INSERT INTO RESTRAUNT (RES_ID,RES_NAME,RES_ph,ADDRESS,RATING) \
      VALUES (1, 'R1', 8865965645, 'Jaipur', 20000.00 )");

conn.execute("INSERT INTO RESTRAUNT (RES_ID,RES_NAME,RES_ph,ADDRESS,RATING) \
      VALUES (2, 'R2', 9876656960, 'Jaipur', 20000.00 )");
             
conn.execute("INSERT INTO RESTRAUNT (RES_ID,RES_NAME,RES_ph,ADDRESS,RATING) \
      VALUES (3, 'R3', 9988665544, 'Jaipur', 20000.00 )");

conn.execute("INSERT INTO RESTRAUNT (RES_ID,RES_NAME,RES_ph,ADDRESS,RATING) \
      VALUES (4, 'R4', 7865666632, '', 20000.00 )");
conn.commit()
print "Records created successfully";
conn.close()