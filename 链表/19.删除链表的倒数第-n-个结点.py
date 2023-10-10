#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建一个虚拟节点，将其指向头节点
        dummy = ListNode(-1, head)
        # 初始化两个指针p1和p2，都指向虚拟节点
        p1 = dummy
        p2 = dummy
        # 将p1指针移动n个节点
        for i in range(n):
            p1 = p1.next
        # 同时移动p1和p2指针，直到p1指向链表末尾
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        # 删除p2指针所指节点的下一个节点
        p2.next = p2.next.next
        # 返回虚拟节点的下一个节点作为新的头节点
        return dummy.next

# @lc code=end
