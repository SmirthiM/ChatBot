import _thread
import time
def a(msg):
    count = 0
    while count < 5:
        count += 1
        time.sleep(3)
        print(msg)
def b(msg):
    count = 0
    while count < 5:
        count += 1
        time.sleep(5)
        print(msg)
try:
    _thread.start_new_thread(a,("Thread1" ,))
    _thread.start_new_thread(a,("Thread2",))
except:
    print("error")
while 1:
    pass
