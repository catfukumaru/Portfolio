#Write a Python program that creates two threads to find and print even and odd numbers from 30 to 50.
import threading
import time
def even(num):
    if (num%2==0):
        print("even")

    time.sleep(1)
    

def odd(num):
    if (num%2!=0):
        print("odd")
    time.sleep(1)



for i in range(30,50):

    t1 = threading.Thread(target=even, args=(i,))
    t2 = threading.Thread(target=odd, args=(i,))
    t1.start()
    t2.start()

t1.join()
t1.join()

print("it is done")

# wrong. did not read properly.but the method is correct. instead of printing odd and even you shoudl just print the numbers


    

