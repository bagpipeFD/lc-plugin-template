#
# @lc app=leetcode.cn id=1438 lang=python3
# @lcpr version=30403
#
# [1438] 绝对差不超过限制的最长连续子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import deque
class MonotoicQueue:
    def __init__(self):
        self.q = deque()
        self.maxq = deque()
        self.minq = deque()
    def push(self,elem:int):
        self.q.append(elem)
        while self.maxq and self.maxq[-1]<elem:
            self.maxq.pop()
        self.maxq.append(elem)
        
        while self.minq and self.minq[-1]>elem:
            self.minq.pop()
        self.minq.append(elem)
    def max(self) -> int:
        return self.maxq[0]
    def min(self) -> int:
        return self.minq[0]
    def pop(self) -> int:
        deleteval = self.q.popleft()
        if deleteval == self.maxq[0]:
            self.maxq.popleft()
        if deleteval ==self.minq[0]:
            self.minq.popleft()
        return deleteval
    def size(self) -> int:
        return len(self.q)
    def isEmpty(self) ->bool:
        return not self.q
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left,right = 0,0
        windowSize = 0
        res = 0
        window = MonotoicQueue()
        while right <len(nums):
            window.push(nums[right])
            right +=1
            windowSize+=1
            while window.max()-window.min()>limit:
                window.pop()
                left+=1
                windowSize-=1
            res = max(res,windowSize)
        return res        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [8,2,4,7]\n4\n
# @lcpr case=end

# @lcpr case=start
# [10,1,2,4,7,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,2,2,2,4,4,2,2]\n0\n
# @lcpr case=end

#

