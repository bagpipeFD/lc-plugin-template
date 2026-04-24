#
# @lc app=leetcode.cn id=933 lang=python3
# @lcpr version=30403
#
# [933] 最近的请求次数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0]<t-3000:
            self.q.popleft()
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# ["RecentCounter","ping","ping","ping","ping"]\n[[],[1],[100],[3001],[3002]]\n
# @lcpr case=end

#

