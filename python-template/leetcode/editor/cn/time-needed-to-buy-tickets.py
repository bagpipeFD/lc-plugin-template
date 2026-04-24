#
# @lc app=leetcode.cn id=2073 lang=python3
# @lcpr version=30400
#
# [2073] 买票需要的时间
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        i = 0
        res = 0
        for i,t in enumerate(tickets):
            queue.append([i,tickets[i]])
        while res >=0:
            [i,t] = queue.popleft()
            print(i,t)
            t-=1
            res+=1
            if i ==k and t==0:
                break
            elif t!=0:
                queue.append([i,t])

        return res 
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [2,3,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,1]\n0\n
# @lcpr case=end

#

