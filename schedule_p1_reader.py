import schedule
import time

def job():
    print"P1 read started..." + time.strftime("%Y-%m-%d %H:%M:%S")
    execfile("read_p1_telegram.py")
    execfile("process_p1_telegram.py") 
    execfile("sqlite_log.py")

print("Reader will launch in 60 sec")
time.sleep(60)
print("reader will relaund every 5 sec")
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
