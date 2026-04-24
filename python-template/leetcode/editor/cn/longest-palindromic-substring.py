#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30400
#
# [5] 最长回文子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) ==0 or len(s)==1:
            return s
        res = ""
        for i in range(len(s)):
            s1 = self.palindrome(s,i,i)
            s2 = self.palindrome(s,i,i+1)
            if len(s1)> len(res):
                res = s1
            if len(s2)> len(res):
                res = s2
        return res        
        
        
    def palindrome(self,s:str,l:int,r:int):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l -=1
            r +=1
        return s[l+1:r]
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

