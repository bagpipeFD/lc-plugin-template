#
# @lc app=leetcode.cn id=641 lang=python3
# @lcpr version=30400
#
# [641] 设计循环双端队列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import deque
class MyArrayDeque:
    INIT_CAP = 2
    def __init__(self,init_cap=INIT_CAP):
        self.size = 0
        self.data = [None]*init_cap
        self.first = self.last = 0
    
    def isEmpty(self):
        return self.size==0
    def getSize(self):
        return self.size
    def getFirst(self):
        if self.isEmpty():
           raise IndexError("getFirst from empty deque")
        return self.data[self.first]
    def getLast(self):
        if self.isEmpty():
           raise IndexError("getLast from empty deque")        
        if self.last == 0:
            return self.data[len(self.data)-1]
        return self.data[self.last-1]
    def addFirst(self,e):
        if self.size==len(self.data):
            self.resize(self.size*2)
        if self.first == 0:
            self.first = len(self.data)-1
        else:
            self.first -=1
        self.data[self.first]= e
        self.size+=1
    def addLast(self,e):
        if self.size==len(self.data):
            self.resize(self.size*2)
        self.data[self.last] = e
        self.last+=1
        if self.last == len(self.data):
            self.last =0
        self.size +=1
    def resize(self,new_cap):
        temp = [None]*new_cap
        for i in range(self.size):
            temp[i]=self.data[(self.first+i)%len(self.data)]
        self.first = 0
        self.last = self.size
        self.data = temp
    def removeFirst(self):
        if self.isEmpty():
           raise IndexError("removeFirst from empty deque")        
        if self.size == len(self.data)//4:
            self.resize(len(self.data)//2)
        old_val = self.data[self.first]
        self.data[self.first]=None
        self.first +=1
        if self.first == len(self.data):
            self.first = 0
        self.size -=1
        return old_val
    def removeLast(self):
        if self.isEmpty():
           raise IndexError("removeLast from empty deque")        
        if self.size == len(self.data)//4:
            self.resize(len(self.data)//2)    
        if self.last ==0:
            self.last = len(self.data) -1
        else:
            self.last -=1
        old_val = self.data[self.last]
        self.data[self.last] = None
        self.size -=1
        return old_val
             
        
     
class MyCircularDeque:

    def __init__(self, k: int):
        self.maxcap = k
        self.list = MyArrayDeque()
        

    def insertFront(self, value: int) -> bool:
        if self.list.getSize()==self.maxcap:
            return False
        self.list.addFirst(value)
        return True        
        
        

    def insertLast(self, value: int) -> bool:
        if self.list.getSize()==self.maxcap:
            return False
        self.list.addLast(value)
        return True

    def deleteFront(self) -> bool:
        if self.list.isEmpty():
            return False
        else:
            self.list.removeFirst()
            return True

    def deleteLast(self) -> bool:
        if self.list.isEmpty():
            return False
        else:
            self.list.removeLast()
            return True        

    def getFront(self) -> int:
        if self.list.isEmpty():
            return -1            
        return self.list.getFirst()
        

    def getRear(self) -> int:
        if self.list.isEmpty():
            return -1         
        return self.list.getLast()
        

    def isEmpty(self) -> bool:
        return self.list.isEmpty()
        

    def isFull(self) -> bool:
        return self.list.getSize()==self.maxcap
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# ["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]\n[[3],[1],[2],[3],[4],[],[],[],[4],[]]\n
# @lcpr case=end

#

