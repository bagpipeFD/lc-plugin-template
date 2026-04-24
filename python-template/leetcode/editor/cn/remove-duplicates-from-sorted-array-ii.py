#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=30400
#
# [80] 删除有序数组中的重复项 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow,fast = 0,0
        count = 1
        while fast< len(nums):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow] = nums[fast]
                count=1
            elif slow<fast and count<=2:
                slow+=1
                nums[slow] = nums[fast]
                count+=1
            fast +=1
            count+=1
        return slow+1
        
            

                            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

