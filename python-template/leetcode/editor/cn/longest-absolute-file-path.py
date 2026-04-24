#
# @lc app=leetcode.cn id=388 lang=python3
# @lcpr version=30400
#
# [388] 文件的最长绝对路径
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stk = []
        max_len = 0
        for part in input.split('\n'):
            level = part.rfind('\t')+1
            while level <len(stk):
                stk.pop()
            stk.append(len(part)-level)
            if "." in part:
                total_length = sum(stk) + len(stk) -1
                max_len = max(max_len,total_length)
        return max_len
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"\n
# @lcpr case=end

# @lcpr case=start
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

