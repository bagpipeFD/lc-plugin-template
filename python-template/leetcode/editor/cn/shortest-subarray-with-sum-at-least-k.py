#
# @lc app=leetcode.cn id=862 lang=python3
# @lcpr version=30403
#
# [862] 和至少为 K 的最短子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import deque
class MonotonicQueue:
    def __init__(self):
        self.q = deque()
        self.maxq = deque()
        self.minq = deque()
    def push(self,elem):
        self.q.append(elem)
        while self.maxq and self.maxq[-1]<elem:
            self.maxq.pop()
        self.maxq.append(elem)
        while self.minq and self.minq[-1]>elem:
            self.minq.pop()
        self.minq.append(elem)        
    def pop(self) -> int:
        deleteval = self.q.popleft()
        if deleteval == self.maxq[0]:
            self.maxq.popleft()
        if deleteval == self.minq[0]:
            self.minq.popleft()
        return deleteval
    def max(self) -> int:
        return self.maxq[0]
    def min(self) -> int:
        return self.minq[0]
    def size(self) ->int:
        return len(self.q)
    def isEmpty(self) -> bool:
        return not self.q 
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0] *(n+1)
        preSum[0] = 0
        for i in range(1,n+1):
            preSum[i] = preSum[i-1]+nums[i-1]
        window = MonotonicQueue()
        left,right = 0,0
        length = float('inf')
        while right<n+1:
            window.push(preSum[right])
            right+=1
            while right <len(preSum) and not window.isEmpty() and preSum[right]-window.min()>=k:
                length = min(length,right-left)
                window.pop()
                left+=1
        return -1 if length == float('inf') else length
            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,2]\n3\n
# @lcpr case=end

#

