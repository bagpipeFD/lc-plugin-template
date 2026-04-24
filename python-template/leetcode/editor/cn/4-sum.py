#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30400
#
# [18] 四数之和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue                 
            triples = self.threeSum(nums,i+1,target-nums[i])
            for triple in triples:
                triple.append(nums[i])
                res.append(triple)            
        return res                  
        
    def threeSum(self, nums: list[int],start:int,target:int) -> list[list[int]]:
        n = len(nums)
        res = []
        i = start
        for i in range(start, n):
            if i > start and nums[i] == nums[i - 1]:
                continue            
            tuples = self.twoSumTarget(nums,i+1,target-nums[i])
            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)
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
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#

