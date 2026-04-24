#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30400
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return[-1,-1]
        left,right = 0,len(nums)-1
        side = 0
        res = []
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]>target:
                right = mid -1
            elif nums[mid]<target:
                left = mid+1
            elif nums[mid]==target:
                right = mid-1
        if left<0 or left>=len(nums) :
            return [-1,-1]        
        if nums[left] != target:
            return [-1,-1]   
        res.append(left)     
        left,right = 0,len(nums)-1                      
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]>target:
                right = mid -1
            elif nums[mid]<target:
                left = mid+1
            elif nums[mid]==target:
                left = mid+1
        if right<0 or right>=len(nums) :
            return [-1,-1]        
        if nums[right] != target:
            return [-1,-1]              
        res.append(right) 
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

