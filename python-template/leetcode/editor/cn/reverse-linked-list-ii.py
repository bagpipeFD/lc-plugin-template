#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30400
#
# [92] 反转链表 II
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
    def __init__(self):
        self.successor =None
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left ==1:
            return self.reverseN(head,right-left+1)
        
        head.next = self.reverseBetween(head.next,left-1,right-1)
        return head
    
    def reverseN(self,head: Optional[ListNode],n:int)->Optional[ListNode]:
        if n ==1:
            self.successor = head.next
            return head
        
        
        last = self.reverseN(head.next,n-1)
        head.next.next = head
        head.next = self.successor
        return last
    
      # @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

