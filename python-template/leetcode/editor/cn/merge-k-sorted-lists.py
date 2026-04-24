#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30307
#
# [23] 合并 K 个升序链表
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        dummy = ListNode(-1)
        p = dummy
        pq = []
        
        for i,head in enumerate(lists):
            if head:
                heapq.heappush(pq,(head.val,i,head))
        while pq:
            val,i,node = heapq.heappop(pq)
            p.next = node
            p = p.next
            
            if node.next:
                heapq.heappush(pq,(node.next.val,i,node.next))
        return dummy.next

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

