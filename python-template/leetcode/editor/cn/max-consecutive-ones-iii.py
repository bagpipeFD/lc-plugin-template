#
# @lc app=leetcode.cn id=1004 lang=python3
# @lcpr version=30400
#
# [1004] 最大连续1的个数 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left,right = 0,0
        cur = 0
        max_len = 0
        while right<n:
            if nums[right]==0:
                cur +=1
            right +=1
            while cur>k and left<right:
                if nums[left]==0:
                    cur -=1
                left+=1
            max_len = max(max_len,right-left)    
        return max_len            
                
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,1,1,0,0,0,1,1,1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
# @lcpr case=end

#

