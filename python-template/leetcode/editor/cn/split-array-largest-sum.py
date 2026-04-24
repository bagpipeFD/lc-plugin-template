#
# @lc app=leetcode.cn id=410 lang=python3
# @lcpr version=30400
#
# [410] 分割数组的最大值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left,right = max(nums),sum(nums)
        while left<=right:
            mid = left+(right-left)//2
            flag = self.f(nums,mid)
            if flag> k:
                left = mid+1
            else:
                right = mid -1
        return left
        
        
        
        
    def f(self, nums: List[int], x: int) -> int:
        sums = 0
        i = 0
        while i < len(nums):
            cap = x
            while i < len(nums):
                if cap < nums[i]:
                    break
                else:
                    cap -= nums[i]
                    i += 1
            sums += 1
        return sums
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [7,2,5,10,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

#

