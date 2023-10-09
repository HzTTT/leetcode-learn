#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# @lc code=start
# Definition for singly-linked list.
import heapq

ListNode.__lt__ = lambda self, other: self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode(-1)
        p = dummy
        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq,(head.val, head))

        while pq:
            node = heapq.heappop(pq)[1]
            p.next = node
            if node.next:
                heapq.heappush(pq,(node.next.val, node.next))
            p = p.next

        return dummy.next
# @lc code=end