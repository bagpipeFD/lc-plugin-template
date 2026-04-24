#
# @lc app=leetcode.cn id=1201 lang=python3
# @lcpr version=30400
#
# [1201] 丑数 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = int(2e9)
        
        while left<=right:
            mid =left + (right-left)//2
            if self.f(mid,a,b,c)<n:
                left = mid+1
            else:
                right = mid-1
        return left
            
            
    def gcd(self,a:int,b:int)->int:
        if a<b:
            return self.gcd(b,a)
        if b == 0:
            return a
        return self.gcd(b,a%b)
    
    
    def lcm(self,a:int,b:int) ->int:
        
        return a*b//self.gcd(a,b)

    def f(self,num:int,a:int,b:int,c:int)->int:
        seta, setb, setc = num//a,num//b,num//c
        setab = num//self.lcm(a,b)
        setbc = num//self.lcm(b,c)
        setac = num//self.lcm(a,c)
        setabc = num//self.lcm(a,self.lcm(b,c))
        
        return seta+setb+setc-setab-setac-setbc+setabc
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# 3\n2\n3\n5\n
# @lcpr case=end

# @lcpr case=start
# 4\n2\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# 5\n2\n11\n13\n
# @lcpr case=end

#

