#
# @lc app=leetcode.cn id=581 lang=python3
# @lcpr version=30403
#
# [581] 最短无序连续子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = float('inf')
        right = float('-inf')
        incr_stk= []
        for i in range(n):
            while incr_stk and nums[i]<nums[incr_stk[-1]]:
                left = min(left,incr_stk.pop())                
            incr_stk.append(i)
        decr_stk=[]
        for i in range(n-1,-1,-1):
            while decr_stk and nums[i]>nums[decr_stk[-1]]:
                right = max(right,decr_stk.pop())
            decr_stk.append(i)
        if left == float('inf') or right == float('-inf'):
            return 0 
        return right - left +1
            
                                                          
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [2,6,4,8,10,9,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

