#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        lenA, lenB =0,0
        while p:
            p = p.next
            lenA += 1
        p = headB
        while p:
            p = p.next
            lenB += 1
        
        p1, p2 = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                p1 = p1.next
        else:
            for i in range(lenB - lenA):
                p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
        
# @lc code=end
