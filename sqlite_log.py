import sqlite3
import os.path
import hashlib

if(len(str(serial_number))):
	db_name = hashlib.md5(str(serial_number)).hexdigest()
	db = db_name+'.db'
	conn = sqlite3.connect(db)
	c = conn.cursor()

# Create table (if not already there)
#if os.path.isfile(db):
#c.execute('''CREATE TABLE loads (date datetime, lowtarif_demand real, hightarif_demand real, lowtarif_supply real, hightarif_supply real, demand_power real, supply_power real, gas_demand real)''')

# Insert a row of data
	c.execute("INSERT INTO loads VALUES (datetime(),"+str(lowtarif_demand)+","+str(hightarif_demand)+","+str(lowtarif_supply)+","+str(hightarif_supply)+","+str(demand_power)+","+str(supply_power)+","+str(gas_demand)+")")
#('lowtarif_demand', 3916784.0, 'Wh')
#('hightarif_demand', 3449407.0, 'Wh')
#('lowtarif_supply', 1068.0, 'Wh')
#('hightarif_supply', 575.0, 'Wh')
#('demand_power', 150.0, 'W')
#('supply_power', 0.0, 'W')
#('gas_demand', 1694.709, 'm3')

# Save (commit) the changes
	conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
	conn.close()
