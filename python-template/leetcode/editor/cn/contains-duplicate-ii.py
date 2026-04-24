#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30400
#
# [219] 存在重复元素 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        left,right = 0,0
        windowSet = set()
        while right<n:
            c = nums[right]         
            right +=1
            if c in windowSet:
                return True
            windowSet.add(c)
            while left<right and right-left>k:
                windowSet.discard(nums[left])
                left +=1
            
        return False
                

              
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#

