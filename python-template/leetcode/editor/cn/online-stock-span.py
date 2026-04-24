#
# @lc app=leetcode.cn id=901 lang=python3
# @lcpr version=30403
#
# [901] 股票价格跨度
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.stk = []
        

    def next(self, price: int) -> int:
        count =1
        while self.stk and price>=self.stk[-1][0]:
            prev = self.stk.pop()
            count+=prev[1]
        self.stk.append([price,count])
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# ["StockSpanner","next","next","next","next","next","next","next"]\n[[],[100],[80],[60],[70],[60],[75],[85]]\n
# @lcpr case=end

#

