# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 02:54:36 2018

@author: arpit
"""

import csv
 
# field names
fields = ['Res_Name', 'Res_code', 'Res_Address', 'Res_phone']
 
# data rows of csv file
rows = [ ['R1', '1', 'A', '90'],
         ['R2', '2', 'B', '91'],
         ['R3', '3', 'C', '93'],
         ['R4', '4', 'D', '95'],
         ['R5', '5', 'E', '78'],
         ['R6', '6', 'F', '91']]
 
filename = "res_records.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)