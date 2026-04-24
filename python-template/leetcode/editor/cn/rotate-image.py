#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30400
#
# [48] 旋转图像
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
        for row in matrix:
            self.reverseRow(row)
        return matrix
        
        
    def reverseRow(self,temp:List[int])->List[int]:
        i,j = 0,len(temp)-1
        while i<j:
            temp[i],temp[j]=temp[j],temp[i]
            i+=1
            j-=1
        return temp
        
                
                
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

