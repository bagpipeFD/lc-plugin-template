#
# @lc app=leetcode.cn id=1329 lang=python3
# @lcpr version=30400
#
# [1329] 将矩阵按对角线排序
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        diagonals = {}
        
        for i in range(m):
            for j in range(n):
                diagonalID = i - j
                if diagonalID not in diagonals:
                    diagonals[diagonalID] = []
                diagonals[diagonalID].append(mat[i][j])
        
        for _,value in diagonals.items():
            value.sort(reverse = True)
            
        for i in range(m):
            for j in range(n):
                value = diagonals[i - j]
                mat[i][j] = value.pop()
        return mat
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[3,3,1,1],[2,2,1,2],[1,1,1,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]\n
# @lcpr case=end

#

