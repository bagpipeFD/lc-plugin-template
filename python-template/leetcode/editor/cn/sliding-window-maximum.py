#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30403
#
# [239] 滑动窗口最大值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class MonotonicQuene:
    def __init__(self):
        self.maxq = []
    def push(self,n):
        while self.maxq and self.maxq[-1]<n:
            self.maxq.pop()
        self.maxq.append(n)
    def max(self):
        return self.maxq[0]
    def pop(self,n):
        if n == self.maxq[0]:
            self.maxq.pop(0)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQuene()
        res = []
        for i in range(len(nums)):
            if i <k-1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i-k+1])
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

