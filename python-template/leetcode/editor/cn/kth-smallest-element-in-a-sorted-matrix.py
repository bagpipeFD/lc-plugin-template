#
# @lc app=leetcode.cn id=378 lang=python3
# @lcpr version=30307
#
# [378] 有序矩阵中第 K 小的元素
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        for i in range(len(matrix)):
            heapq.heappush(pq,(matrix[i][0],i,0))
        res = -1
        while pq and k>0:
            val,i,j = heapq.heappop(pq)
            res = val
            k -=1
            if j+1<len(matrix):
                heapq.heappush(pq,(matrix[i][j+1],i,j+1))
        return res
                
                
                

                        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[1,5,9],[10,11,13],[12,13,15]]\n8\n
# @lcpr case=end

# @lcpr case=start
# [[-5]]\n1\n
# @lcpr case=end

#

