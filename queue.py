a = []

a.insert(0, 12.1)
a.insert(0, 157.2)
a.insert(0, 1548.48)
print(a)
a.pop()
print(a)

from collections import deque
import time
import threading



q = deque()

q.appendleft(4)
q.appendleft(88)
q.appendleft(584)
q.appendleft(848484)
print(q)

q.pop()
print(q)

class Queue:
    
    def __init__(self) -> None:
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        self.buffer.pop()
        
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

def order(arr):
    dq = Queue()
    
    for item in arr:
        dq.appendleft(item)
        time.sleep(0.5)

    return dq

def serve(dq):
    print(dq.pop())
    time.sleep(2)


    
    
    

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    
    t1 = threading.Thread(order, args=orders)
    t2 = threading.Thread(serve, args=t1)
    t1.start()
    t2.start()
    
    t1.join()
    t2.join(2)
    dq = Queue()
    
