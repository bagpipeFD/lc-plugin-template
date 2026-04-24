#
# @lc app=leetcode.cn id=977 lang=python3
# @lcpr version=30400
#
# [977] 有序数组的平方
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        n = len(nums)
        newnums = [0]* n
        
        left,right = 0,n-1
        p = n-1

        while  left<=right:
            if abs(nums[left])>=abs(nums[right]):
                newnums[p] = abs(nums[left])**2
                left+=1
            else:
                newnums[p] = abs(nums[right])**2
                right-=1
            p-=1
            
        return newnums

        
            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [-4,-1,0,3,10]\n
# @lcpr case=end

# @lcpr case=start
# [-7,-3,2,3,11]\n
# @lcpr case=end

#

