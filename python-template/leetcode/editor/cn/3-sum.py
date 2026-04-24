#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30400
#
# [15] 三数之和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
from collections import defaultdict


# @lc code=start
class Solution:
    def threeSum(self, nums: list[int],target:int=0) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i<n:
            tuples = self.twoSumTarget(nums,i+1,target-nums[i])
            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)
            while i<n-1 and nums[i] ==nums[i+1]:
                i +=1
            i+=1
        return res





    def twoSumTarget(self,nums: list[int],start:int,target:int):
        lo = start
        hi = len(nums)-1
        res = []
        while lo<hi:
            left = nums[lo]
            right=nums[hi]
            sums = nums[lo]+nums[hi]
            if sums>target:
                while lo < hi and nums[hi] == right:
                    hi -=1
            if sums<target:
                while lo < hi and nums[lo] == left:
                    lo +=1          
            if sums==target:
                res.append([left,right])
                while lo < hi and nums[hi] == right:
                    hi -=1
                while lo < hi and nums[lo] == left:
                    lo +=1                                         
                
        return res
      
                 
        

                
                            
        
    

                
                        

    
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

