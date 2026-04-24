#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30400
#
# [20] 有效的括号
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in '{([':
                stk.append(c)        
            else:
                if stk and self.leftOf(c) == stk[-1]:
                    stk.pop()
                else:
                    return False
        return len(stk)==0
        
        
        
        
    def leftOf(self,c:str) -> str:
        if c ==')':
            return '('
        elif c == '}':
            return '{'
        elif c == ']':
            return '['
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#

