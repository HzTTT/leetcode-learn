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
        
        dummy = ListNode(-1)  # 创建一个虚拟节点作为合并后链表的头节点
        p = dummy  # 用于遍历合并后链表的指针
        pq = []  # 创建一个优先队列（最小堆）用于存储各个链表的头节点
        
        # 将每个链表的头节点加入优先队列
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, head))
        
        # 从优先队列中取出最小的节点并加入合并后链表中，同时将该节点的下一个节点加入优先队列
        while pq:
            node = heapq.heappop(pq)[1]
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
            p = p.next
        
        return dummy.next
# @lc code=end