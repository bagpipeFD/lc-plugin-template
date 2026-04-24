#
# @lc app=leetcode.cn id=150 lang=python3
# @lcpr version=30400
#
# [150] 逆波兰表达式求值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token in '+-*/':
                a = stk.pop()
                b = stk.pop()
                if token == '+':
                    stk.append(a+b)
                elif token == '-':
                    stk.append(b-a)
                elif token == '*':
                    stk.append(a*b)
                elif token =='/':
                    stk.append(int(b/a))
            else:
                stk.append(int(token))
        return stk.pop()
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#

