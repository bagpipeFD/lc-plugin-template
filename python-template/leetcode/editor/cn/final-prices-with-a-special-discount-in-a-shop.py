#
# @lc app=leetcode.cn id=1475 lang=python3
# @lcpr version=30403
#
# [1475] 商品折扣后的最终价格
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        div = [n]*n
        stk = []
        res = []
        for i in range(n-1,-1,-1):
            while stk and prices[i]< stk[-1]:
                stk.pop()
            div[i] = prices[i] - 0 if not stk else prices[i]-stk[-1]
            stk.append(prices[i])
        return div    

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [8,4,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [10,1,1,6]\n
# @lcpr case=end

#

