#coding = utf-8
import threading

def sum(a):
    print(a + 5)
def subtract(b):
    print(b - 5)
def multiply(c):
    print(c *2)

#线程列表
threads = []

t1 = threading.Thread(target=sum,args=(0,))
t2 = threading.Thread(target=subtract,args=(0,))
t3 = threading.Thread(target=multiply,args=(1,))

threads.append(t1)
threads.append(t2)
threads.append(t3)


for j in  threads:
    j.start()

