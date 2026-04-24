#
# @lc app=leetcode.cn id=313 lang=python3
# @lcpr version=30400
#
# [313] 超级丑数
#

import sys
import os
import heapq


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pq = []
        for prime in primes:
            heapq.heappush(pq,(1,prime,1))
        
        ugly = [0]*(n+1)
        p = 1
        while p<=n:
            val,prime,index = heapq.heappop(pq)
            
            if val !=ugly[p-1]:
                ugly[p] = val
                p = p+1
            
            heapq.heappush(pq,(ugly[index]*prime,prime,index+1))    
            
        return ugly[n]
                
            
            
        
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# 12\n[2,7,13,19]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[2,3,5]\n
# @lcpr case=end

#

