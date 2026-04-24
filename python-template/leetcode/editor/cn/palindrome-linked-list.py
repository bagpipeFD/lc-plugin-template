#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30400
#
# [234] 回文链表
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if  fast:
            slow = slow.next
            
        p = head
        q = self.reverse(slow)
        
        while q:
            if p.val == q.val:
                p = p.next
                q = q.next
            else:
                return False
        return True
        
    def reverse(self,head: Optional[ListNode])->Optional[ListNode]:
        if not head or not head.next:
            return head
        pre,cur,nxt = None,head,head.next
        while cur :
            cur.next = pre
            pre = cur 
            cur = nxt
            if nxt:
                nxt = nxt.next
        return pre
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

