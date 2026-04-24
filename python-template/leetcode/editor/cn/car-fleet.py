#
# @lc app=leetcode.cn id=853 lang=python3
# @lcpr version=30403
#
# [853] 车队
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append([position[i],speed[i]])
        cars.sort(key=lambda x:x[0])
        time = []
        for car in cars:
            time.append((target-car[0])/car[1])
        res = 0
        max_time = 0
        for i in range(n-1,-1,-1):
            if time[i]>max_time:
                max_time = time[i]
                res +=1            
        return res
            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# 12\n[10,8,0,5,3]\n[2,4,1,1,3]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[3]\n[3]\n
# @lcpr case=end

# @lcpr case=start
# 100\n[0,2,4]\n[4,2,1]\n
# @lcpr case=end

#

