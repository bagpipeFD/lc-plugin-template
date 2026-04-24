#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30400
#
# [143] 重排链表
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
    def reorderList(self, head: ListNode) -> None:
        stk = []
        # 先把所有节点装进栈里，得到倒序结果
        p = head
        while p is not None:
            stk.append(p)
            p = p.next

        p = head
        while p is not None:
            # 链表尾部的节点
            lastNode = stk.pop()
            next = p.next
            if lastNode == next or lastNode.next == next:
                # 结束条件，链表节点数为奇数或偶数时均适用
                lastNode.next = None
                break
            p.next = lastNode
            lastNode.next = next
            p = next

        
        """
        Do not return anything, modify head in-place instead.
        """
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

