#
# @lc app=leetcode.cn id=225 lang=python3
# @lcpr version=30400
#
# [225] 用队列实现栈
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()
        self.topelem = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.topelem = x

    def pop(self) -> int:
        temp = self.q.pop()
        if self.q:
            self.topelem = self.q[-1]
        else:
            self.topelem = None
        return temp
        
        

    def top(self) -> int:
        return self.topelem
        

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# ["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]\n
# @lcpr case=end

#

