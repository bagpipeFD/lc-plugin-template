#
# @lc app=leetcode.cn id=1109 lang=python3
# @lcpr version=30400
#
# [1109] 航班预订统计
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0]* n
        df = self.Difference(nums)
        for booking in bookings:
            i = booking[0] -1
            j = booking[1] -1
            val = booking[2]
            df.increment(i, j, val)
        return df.result()
        
        
        
        
    class Difference:
    
        def __init__(self,nums):
            assert len(nums)>0
            self.diff = [0] *len(nums)
            self.diff[0] = 0
            for i in range(1,len(nums)):
                self.diff[i] = nums[i] - nums[i-1]
        def increment(self,i,j,val):
            self.diff[i] += val            
            if j+1<len(self.diff):
                self.diff[j+1] -= val
        def result(self):
            res = [0]*len(self.diff)
            res[0] = self.diff[0]
            for i in range(1,len(self.diff)):
                res[i] = res[i-1]+self.diff[i]
            return res 
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[1,2,10],[2,3,20],[2,5,25]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,10],[2,2,15]]\n2\n
# @lcpr case=end

#

