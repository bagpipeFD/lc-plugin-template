#
# @lc app=leetcode.cn id=61 lang=python3
# @lcpr version=30400
#
# [61] 旋转链表
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
           return head
        p,q = head,head
        length = 0
        while p is not None:
             length +=1
             p = p.next
        k = k%length

        for i in range(k):
            nxt = q.next
            cur = q
            while nxt.next is not None:
                cur = nxt
                nxt = nxt.next
            nxt.next = q
            cur.next = None
            q = nxt
        return q 
            
                    



    def reverse(self,head: Optional[ListNode]):
        if head is None or head.next is None:
            return head
        pre,cur,nxt = None,head,head.next
        while cur is not None:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt is not None:
                nxt = nxt.next
        return pre
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#

