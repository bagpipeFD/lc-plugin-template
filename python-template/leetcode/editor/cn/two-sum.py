#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30400
#
# [1] 两数之和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = {}
        res =  []
        for i,val in enumerate(nums):
            if target-val not in records:
                records[val]= i
            else:
                result = [records[target-val],i]
                res.append(result)
        return res.pop()
                
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

