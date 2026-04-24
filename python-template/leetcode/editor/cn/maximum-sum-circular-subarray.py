#
# @lc app=leetcode.cn id=918 lang=python3
# @lcpr version=30403
#
# [918] 环形子数组的最大和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import deque
class MonotonicQuere:
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
    def pop(self)->int:
        deleteval = self.q.popleft()
        if deleteval == self.maxq[0]:
            self.maxq.popleft()
        if deleteval ==self.minq[0]:
            self.minq.popleft()
        return deleteval
    def max(self)->int:
        return self.maxq[0]
    def min(self)->int:
        return self.minq[0]
    def size(self)->int:
        return len(self.q)
    def isEmpty(self)->bool:
        return not self.q    
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0]*(2*n+1)
        preSum[0] = 0
        for i in range(1,len(preSum)):
            preSum[i] = preSum[i-1]+nums[(i-1)%n]
        maxSum = float('-inf')
        window = MonotonicQuere()
        window.push(preSum[0])
        for i in range(1,len(preSum)):
            maxSum = max(maxSum,preSum[i]-window.min())
            if window.size() == n:
                window.pop()
            window.push(preSum[i])
        return maxSum
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,-2,3,-2]\n
# @lcpr case=end

# @lcpr case=start
# [5,-3,5]\n
# @lcpr case=end

# @lcpr case=start
# [-3,-2,-3]\n
# @lcpr case=end

#

