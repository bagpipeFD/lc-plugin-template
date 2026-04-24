#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30400
#
# [59] 螺旋矩阵 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        u,d = 0,n-1
        l,r = 0,n-1
        p = 1
        
        while p<=n*n:
            if u <= d:
                for i in range(l ,r+1):
                    matrix[u][i] = p
                    p+=1
                u+=1
            if l<=r:
                for j in range(u,d+1):
                    matrix[j][r] = p
                    p+=1
                r-=1
            if u<=d:
                for i in range(r,l-1,-1):
                    matrix[d][i] = p
                    p+=1
                d-=1
            if l<=r:
                for j in range(d,u-1,-1):
                    matrix[j][l] = p
                    p+=1
                l+=1
        return matrix
                    
                    

                    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

