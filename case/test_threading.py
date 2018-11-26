#coding = utf-8
import threading

def sum(a):
    print(a + 5)

#线程列表
threads = []
for i in range(3):
    print(i)
    t = threading.Thread(target=sum,args=(i,))
    threads.append(t)

for j in  threads:
    j.start()