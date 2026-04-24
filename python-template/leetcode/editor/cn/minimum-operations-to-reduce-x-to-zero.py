#
# @lc app=leetcode.cn id=1658 lang=python3
# @lcpr version=30400
#
# [1658] 将 x 减到 0 的最小操作数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sums = sum(nums)
        n = len(nums)
        target = sums-x
        left,right = 0,0
        window_sum = 0
        max_len = float('-inf')
        while right<n:
            window_sum += nums[right]
            right +=1
            while window_sum>target and left<right:
                window_sum -= nums[left]
                left+=1            
            if window_sum == target:
                max_len = max(max_len,(right-left))
        return -1 if max_len==float('-inf') else n - max_len
        
                
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,1,4,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,20,1,1,3]\n10\n
# @lcpr case=end

#

