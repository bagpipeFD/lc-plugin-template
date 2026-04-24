#
# @lc app=leetcode.cn id=1944 lang=python3
# @lcpr version=30403
#
# [1944] 队列中可以看到的人数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0]*n
        stk = []
        for i in range(n-1,-1,-1):
            count = 0
            while stk and heights[i]>stk[-1]:
                stk.pop()
                count +=1
            res[i] = count if not stk else count+1
            stk.append(heights[i])
            
        return res
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [10,6,8,5,11,9]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,2,3,10]\n
# @lcpr case=end

#

