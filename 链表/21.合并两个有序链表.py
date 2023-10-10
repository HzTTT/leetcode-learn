# @before-stub-for-debug-begin
from python3problem21 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# @lc code=start
# Definition for singly-linked list.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟节点作为合并链表的头部
        dummy = ListNode(-1)
        # 指针 p 用于跟踪合并链表的当前节点
        p = dummy
        # 指针 p1 和 p2 用于遍历链表 list1 和 list2
        p1 = list1
        p2 = list2
        
        # 遍历两个链表，直到其中一个链表到达末尾
        while p1 and p2:
            if p1.val > p2.val:
                # 如果 list1 的值较大，则将 list2 的当前节点追加到合并链表中
                p.next = p2
                p2 = p2.next
            else:
                # 如果 list2 的值较大或相等，则将 list1 的当前节点追加到合并链表中
                p.next = p1
                p1 = p1.next
            # 将指针 p 移动到合并链表的下一个节点
            p = p.next
        
        # 将剩余的节点从 list1 或 list2 追加到合并链表中
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        
        # 返回合并链表的头部
        return dummy.next

# @lc code=end

