#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30400
#
# [287] 寻找重复数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            fast = nums[nums[fast]] 
            slow = nums[slow] 
            if fast == slow:
                break
        slow = 0
        while fast!=slow:
            fast = nums[fast] 
            slow = nums[slow] 
        return slow
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#

