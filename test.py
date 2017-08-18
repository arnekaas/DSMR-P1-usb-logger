import time

print"P1 read test started..." + time.strftime("%Y-%m-%d %H:%M:%S")
execfile("read_p1_telegram.py")
execfile("process_p1_telegram.py") 
execfile("sqlite_log.py")
execfile("mysql_logger.py")
