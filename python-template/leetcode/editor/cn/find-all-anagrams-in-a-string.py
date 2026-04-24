#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30400
#
# [438] 找到字符串中所有字母异位词
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        window,need={},{}
        for c in p:
            need[c]=need.get(c,0)+1
        left,right = 0,0
        vaild=0
        while right < len(s):
            c = s[right]
            right +=1
            if c in need:
                window[c] = window.get(c,0)+1
                if window[c] == need[c]:
                    vaild +=1
            while right -left ==len(p):
                if vaild==len(need):
                    res.append(left)
                d = s[left]
                left+=1
                if d in need and window[d]>0:
                    if window[d]==need[d]:
                        vaild-=1
                    window[d]-=1
        return res
                    
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

