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
        # 计算链表A的长度
        p = headA
        lenA = 0
        while p:
            p = p.next
            lenA += 1
        
        # 计算链表B的长度
        p = headB
        lenB = 0
        while p:
            p = p.next
            lenB += 1
        
        # 将p1和p2分别指向链表A和链表B的头结点
        p1, p2 = headA, headB
        
        # 如果链表A比链表B长，p1先移动到与链表B相同长度的位置
        if lenA > lenB:
            for i in range(lenA - lenB):
                p1 = p1.next
        # 如果链表B比链表A长，p2先移动到与链表A相同长度的位置
        else:
            for i in range(lenB - lenA):
                p2 = p2.next
        
        # 同时移动p1和p2，直到找到相交节点或者到达链表末尾
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
        
# @lc code=end