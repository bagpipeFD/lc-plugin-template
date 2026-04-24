#
# @lc app=leetcode.cn id=88 lang=python3
# @lcpr version=30400
#
# [88] 合并两个有序数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m1,n1 = m-1,n-1
        while m1>=0 and n1>=0:
            if nums1[m1]>=nums2[n1]:
                nums1[m1+n1+1]=nums1[m1]
                m1-=1
            elif nums1[m1]<nums2[n1]:
                nums1[m1+n1+1]=nums2[n1]
                n1-=1
        if n1>=0:
            nums1[0:n1+1]=nums2[0:n1+1]
            
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,0,0,0]\n3\n[2,5,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n[]\n0\n
# @lcpr case=end

# @lcpr case=start
# [0]\n0\n[1]\n1\n
# @lcpr case=end

#

