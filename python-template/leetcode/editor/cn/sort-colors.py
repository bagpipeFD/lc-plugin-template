#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30400
#
# [75] 颜色分类
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return

        p,p1,p2 = 0,0,len(nums)-1
        while p<=p2:
            if nums[p]==0:
                self.swapNums(nums,p,p1)
                p1+=1
            elif nums[p]==2:
                self.swapNums(nums,p,p2)
                p2-=1
            elif nums[p]==1:
                p+=1
            
            if p<p1:
                p=p1
    def swapNums(self, nums: List[int],a:int,b:int) -> None:
        nums[a],nums[b] = nums[b],nums[a]
                

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

