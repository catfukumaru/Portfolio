#Write a Python program to create multiple threads and print their names.
import threading
import time

def func1():
    print("i am thread 1")
    time.sleep(1)

def func2():
    print("i am thread 2")
    time.sleep(1)

def func3():
    print("i am thread 3")
    time.sleep(1)

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t3 = threading.Thread(target=func3)  

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("finished")

#it is wrong but it works.