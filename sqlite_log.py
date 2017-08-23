import sqlite3
import os.path
import hashlib

#check if serial number is given, else save data to example.db
try:
	db_name = hashlib.md5(str(serial_number)).hexdigest() #hash serial number for security reasons (eg. data sharing with no backtrace)
	db = db_name+'.db'
except:
	db = 'example.db'

# Create table (if not database dous not exist)
if os.path.isfile(db):
	print "Saving data to sqlite db: " + db
        conn = sqlite3.connect(db)
        c = conn.cursor()
else:
        conn = sqlite3.connect(db)
        c = conn.cursor()
	c.execute('''CREATE TABLE loads (date datetime, lowtarif_demand real, hightarif_demand real, lowtarif_supply real, hightarif_supply real, demand_power real, supply_power real, gas_demand real)''')

# Insert a row of data
c.execute("INSERT INTO loads VALUES (datetime(),"+str(lowtarif_demand)+","+str(hightarif_demand)+","+str(lowtarif_supply)+","+str(hightarif_supply)+","+str(demand_power)+","+str(supply_power)+","+str(gas_demand)+")")

# Save (commit) the changes and close db
conn.commit()
conn.close()
