#
# @lc app=leetcode.cn id=1094 lang=python3
# @lcpr version=30400
#
# [1094] 拼车
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0]* 10001
        df = self.Difference(nums)
        for trip in trips:
            i = trip[1] 
            j = trip[2] -1
            val = trip[0]
            df.increment(i, j, val)
        return df.result(capacity)        
        
        
        
        
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
        def result(self,k):
            res = [0]*len(self.diff)
            res[0] = self.diff[0]
            if res[0] > k:
                return False           
            for i in range(1,len(self.diff)):
                res[i] = res[i-1]+self.diff[i]
                if res[i]>k:
                    return False
            return True   
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[2,1,5],[3,3,7]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,5],[3,3,7]]\n5\n
# @lcpr case=end

#

