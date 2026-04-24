#
# @lc app=leetcode.cn id=622 lang=python3
# @lcpr version=30400
#
# [622] 设计循环队列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import deque
class ArrayQueue:
    INIT_CAP = 2
    def __init__(self,init_cap = INIT_CAP):
        self.size = 0
        self.data = [None]*init_cap
        self.first = 0
        self.last = 0
    def enqueue(self,e):
        if self.size == len(self.data):
            self.resize(self.size*2)
        self.data[self.last] = e
        self.last+=1
        if self.last == len(self.data):
            self.last = 0
        self.size+=1
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue underflow')
        if self.size == len(self.data)//4:
            self.resize(len(self.data)//2)
        old_val = self.data[self.first]
        self.data[self.first] = None
        self.first +=1
        if self.first ==len(self.data):
            self.first = 0
        self.size -=1
        return old_val 
    def resize(self,new_cap):
        temp = [None]* new_cap
        for i in range(self.size):
            temp[i]=self.data[(self.first+i)%len((self.data))]            
    
        self.first= 0
        self.last= self.size
        self.data = temp  
    def peek_first(self):
        if self.is_empty():
            raise Exception('Queue underflow')
        return self.data[self.first]
            
    def peek_last(self):
        if self.is_empty():
            raise Exception('Queue underflow')        
        if self.last ==0:
            return self.data[len(self.data)-1]
        return self.data[self.last-1]
    def size(self):
        return self.size
    def is_empty(self):
        return self.size == 0

            
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = ArrayQueue(k)
        self.max_cap = k
        

    def enQueue(self, value: int) -> bool:
        if self.q.size == self.max_cap:
            return False
        self.q.enqueue(value)
        return True
        

    def deQueue(self) -> bool:
        if self.q.is_empty():
            return False
        self.q.dequeue()
        return True
        

    def Front(self) -> int:
        if self.q.is_empty():
            return -1
        return self.q.peek_first()
        

    def Rear(self) -> int:
        if self.q.is_empty():
            return -1
        return self.q.peek_last()        

    def isEmpty(self) -> bool:
        return self.q.is_empty()
        

    def isFull(self) -> bool:
        return self.q.size == self.max_cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n[[3],[1],[2],[3],[4],[],[],[],[4],[]]\n
# @lcpr case=end

#

