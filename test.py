import time


print"P1 read test started..." + time.strftime("%Y-%m-%d %H:%M:%S")
execfile("read_p1_telegram.py")
execfile("process_p1_telegram.py") 
execfile("sqlite_log.py")
execfile("mysql_logger.py")

print ("P1 read test started..." + time.strftime("%Y-%m-%d %H:%M:%S"))
try:
    execfile("p1logger.py")
except:
    print("P1 DSMR read failed")

try:
    execfile("process_p1_telegram.py")
    execfile("sqlite_log.py")
except:
    print("Wrong data/telegram recieved?")

try:
    execfile("mysql_logger.py")
except:
    print("mysql save of data failed, please check settings in mysql_logger")
