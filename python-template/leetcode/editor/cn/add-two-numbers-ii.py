#
# @lc app=leetcode.cn id=445 lang=python3
# @lcpr version=30400
#
# [445] 两数相加 II
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 = []
        stk2 = []
        stk = []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        cur = 0
        dummy = ListNode(-1)
        p = dummy
        
        while stk1 or stk2 or cur:
            val = cur
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            cur = val//10
            val = val%10
            stk.append(val)
        while stk:
            p.next = ListNode(stk.pop())
            p = p.next
        return dummy.next 
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [7,2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

#

