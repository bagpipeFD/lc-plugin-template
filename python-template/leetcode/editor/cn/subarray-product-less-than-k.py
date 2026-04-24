#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30400
#
# [713] 乘积小于 K 的子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left,right = 0,0
        product = 1
        res = 0
        while right<n:
            product *= nums[right]
            right+=1
            while left<right and product>=k:
                product//= nums[left]
                left+=1
            res +=right -left
        return res
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

