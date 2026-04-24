#
# @lc app=leetcode.cn id=71 lang=python3
# @lcpr version=30400
#
# [71] 简化路径
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stk = []
        for part in parts:
            if part == "" or part == '.':
                continue
            if part == "..":
                if stk:
                    stk.pop()
                continue
            stk.append(part)
        res = ""
        while stk:
            res = "/"+stk.pop()+res
        return res if res else "/"
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "/home/"\n
# @lcpr case=end

# @lcpr case=start
# "/home//foo/"\n
# @lcpr case=end

# @lcpr case=start
# "/home/user/Documents/../Pictures"\n
# @lcpr case=end

# @lcpr case=start
# "/../"\n
# @lcpr case=end

# @lcpr case=start
# "/.../a/../b/c/../d/./"\n
# @lcpr case=end

#

