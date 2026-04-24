#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30307
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        p1 = dummy
        p2 = dummy
        
        for i in range(n+1):
            p1 = p1.next

        while  p1 :
            p2 = p2.next
            p1 = p1.next
            
        p2.next = p2.next.next
        return dummy.next
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

