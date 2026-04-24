#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30403
#
# [53] 最大子数组和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        dp = nums[0]
        for i in range(1,len(nums)):
            dp = max(nums[i],dp+nums[i])
            res = max(dp,res)
        return res
            
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

