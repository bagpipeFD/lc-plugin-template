#
# @lc app=leetcode.cn id=402 lang=python3
# @lcpr version=30403
#
# [402] 移掉 K 位数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        stk = []
        for c in num:
            while stk and k>0 and c <stk[-1]:
                stk.pop()
                k-=1
            if not stk and c == '0':
                continue
            stk.append(c)
        final_stk = stk[:-k] if k else stk
        result = ''.join(final_stk).lstrip('0')
        return result if result else '0' 
            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "1432219"\n3\n
# @lcpr case=end

# @lcpr case=start
# "10200"\n1\n
# @lcpr case=end

# @lcpr case=start
# "10"\n2\n
# @lcpr case=end

#

