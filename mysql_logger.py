#P1 telegram from smart processor made by Arne
from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
import re


print("The reader has started")
file = 'P1telegrams.txt'
pattern = re.compile("([0-9].[78].[0-9])\(([0-9]*.[0-9]*)\*(k[wW][h]?)?\)")
#read and process the file
for i, line in enumerate(open(file)):
    for match in re.finditer(pattern, line):
        #print 'Found on line %s: %s' % (i+1, match.groups())
	#print 'Power: ' + match.group(2) + match.group(3)
	#print 'Type: ' + match.group(1)
	if '1.7.0' in match.group(1):	
		Power_Consumed = int(float(match.group(2))*1000)
		print ("Power_Consumed: " + str(Power_Consumed) + 'W')
	if '.8.' in match.group(1):
		print (str(int(float(match.group(2))*1000)) + 'Wh')

#regular expression to get values

#save values to local DB
	#CREATE USER 'p1logger'@'localhost' IDENTIFIED BY 'p1logger';
	#CREATE DATABASE  EnergyLogs;
	#GRANT ALL ON EnergyLogs.* TO 'p1logger'@'localhost';
	#GRANT SELECT ON EnergyLogs.* TO 'p1logger'@'*';

# mysql connect
cnx = mysql.connector.connect(user='p1logger',password='p1logger', database='EnergyLogs')
cursor = cnx.cursor()

now = datetime.now()	# +timedelta(hours=1)
data_salary = {'datetime': now}

QUERY = ("INSERT INTO test "
               "(datetime) "
               "VALUES (%s)")

# Insert energy data
data_salary = {
  'datetime': now,
  'emp_no': emp_no,
  'salary': 50000  
}

QUERY = "CREATE TABlE `EnergyLogs`.`test2` ( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, datetime DATETIME );"

cursor.execute(QUERY)
id = cursor.lastrow

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()

