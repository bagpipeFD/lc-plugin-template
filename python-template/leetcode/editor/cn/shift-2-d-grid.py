#
# @lc app=leetcode.cn id=1260 lang=python3
# @lcpr version=30400
#
# [1260] 二维网格迁移
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        mn = m*n
        k = k%mn
        
        self.reverse(grid,mn-k,mn-1)
        self.reverse(grid,0,mn-k-1)
        self.reverse(grid,0,mn-1)
        
        return grid

        
        
        
        
        
        
    def get(self,grid,index):
        n = len(grid[0])
        i,j = divmod(index,n)
        return grid[i][j]
    
    def set(self,grid,index,val):
        n = len(grid[0])
        i,j = divmod(index,n)
        grid[i][j]= val
    
    def reverse(self,grid,i,j):
        while i< j:
            temp = self.get(grid,i)
            self.set(grid,i,self.get(grid,j))
            self.set(grid,j,temp)
            i +=1
            j -=1
            
        
        
        
        

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n9\n
# @lcpr case=end

#

