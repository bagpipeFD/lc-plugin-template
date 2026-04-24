#
# @lc app=leetcode.cn id=395 lang=python3
# @lcpr version=30400
#
# [395] 至少有 K 个重复字符的最长子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        length = 0
        for i in range(1,27):
            length = max(length,self.longestKLetterSubstr(s,k,i))
        return length
    def longestKLetterSubstr(self,s:str,k:int,count:int)->int:
        res = 0
        left,right = 0,0
        windowCount = [0]*26
        windowUniqueCount = 0
        windowValidCount = 0       
        while right<len(s):
            c = s[right]
            if windowCount[ord(c)-ord('a')]==0:
                windowUniqueCount+=1
            windowCount[ord(c)-ord('a')] +=1
            if windowCount[ord(c)-ord('a')] ==k:
                windowValidCount +=1
            right+=1
            while windowUniqueCount >count:
                d = s[left]
                if windowCount[ord(d)-ord('a')]==k:
                    windowValidCount-=1    
                windowCount[ord(d)-ord('a')]-=1
                if windowCount[ord(d)-ord('a')]==0:
                    windowUniqueCount-=1
                left+=1
            if windowValidCount == count:
                res = max(res,right-left)
        return res                
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "aaabb"\n3\n
# @lcpr case=end

# @lcpr case=start
# "ababbc"\n2\n
# @lcpr case=end

#

