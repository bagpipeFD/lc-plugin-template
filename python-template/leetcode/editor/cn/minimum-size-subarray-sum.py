#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30400
#
# [209] 长度最小的子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right = 0,0
        windowSum = 0
        res = float('inf') 
        while right <len(nums):
            c = nums[right]
            windowSum +=c
            right+=1
            while windowSum>=target and left<right:
                res = min(res,right-left)               
                d = nums[left]
                windowSum-=d
                left+=1
                
        return 0 if res == float('inf')  else res
                
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

