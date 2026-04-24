#
# @lc app=leetcode.cn id=373 lang=python3
# @lcpr version=30400
#
# [373] 查找和最小的 K 对数字
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        res = []
        for i in range(len(nums1)):
            heapq.heappush(pq,(nums1[i]+nums2[0],i,0))
        while pq and k>0:
            _,n1,n2 = heapq.heappop(pq)
            k -=1
            pair = [nums1[n1],nums2[n2]]
            res.append(pair)            
            if n2+1<len(nums2):
                heapq.heappush(pq,(nums1[n1]+nums2[n2+1],n1,n2+1))
        return res

        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#

