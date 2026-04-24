#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30400
#
# [54] 螺旋矩阵
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        u,d = 0,m-1
        l,r = 0,n-1
        res = []
        
        while len(res)<m*n:
            if u<=d:
                for j in range(l,r+1):
                    res.append(matrix[u][j])
                u+=1
            if l<=r:
                for i in range(u,d+1):
                    res.append(matrix[i][r])
                r-=1
            if  u<=d:
                for j in range(r,l-1,-1):
                    res.append(matrix[d][j])
                d-=1
            if l<=r:
                for i in range(d,u-1,-1):
                    res.append(matrix[i][l])
                l+=1
        return res
            
                        
        
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

