#
# @lc app=leetcode.cn id=LCR 140 lang=python3
# @lcpr version=30307
#
# [LCR 140] 训练计划 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        p2 = dummy
        for i in range(cnt):
            if p1.next:
                p1 =p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [2,4,7,8]\n1\n
# @lcpr case=end

#

