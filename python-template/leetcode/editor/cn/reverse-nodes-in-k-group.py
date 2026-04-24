#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30400
#
# [25] K 个一组翻转链表
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
        self.successor = None
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        a, b = head,head
        for i in range(k):
            if b:
                b = b.next
            else:
                return head
        
        newhead = self.reverseN(a,k)
        
        a.next = self.reverseKGroup(b,k)
        
        return newhead                

    def reverseN(self,head: Optional[ListNode], k: int):
        if k==1:
            self.successor = None
            return head
        last = self.reverseN(head.next,k-1)
        head.next.next = head
        head.next = self.successor
        return last
        

        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

