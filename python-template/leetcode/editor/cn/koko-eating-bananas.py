#
# @lc app=leetcode.cn id=875 lang=python3
# @lcpr version=30400
#
# [875] 爱吃香蕉的珂珂
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)
        left,right = 1,piles[n-1]
        
        while left<= right:
            mid = left+(right-left)//2
            t = self.timeSum(piles,mid)
            if t> h:
                left = mid+1
            elif t<h:
                right = mid-1
            elif t == h:
                right = mid -1
        return left        
            
    def timeSum(self,piles: List[int],k:int)->int:
        times = 0
        for i in range(len(piles)):
            times += (piles[i] + k - 1) // k
        return times
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#

