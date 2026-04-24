#
# @lc app=leetcode.cn id=1011 lang=python3
# @lcpr version=30400
#
# [1011] 在 D 天内送达包裹的能力
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left<=right:
            mid =left + (right -left)//2
            n = self.daysSum(weights,mid)
            if n>days:
                left = mid+1
            elif n<=days:
                right = mid -1
            
        return left
        
    def daysSum(self,weights: List[int], k: int) ->int:
        cur = 0
        p,q = 0,0 
        days = 0
        while p <len(weights):
            cur += weights[p]
            if cur == k:
                days +=1
                cur = 0
                q = p
            elif cur >k:
                days +=1
                cur = 0
                p -=1
                q = p
            p+=1  
        if p-q>1:
            days +=1
        return days
                        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,4,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,1]\n4\n
# @lcpr case=end

#

