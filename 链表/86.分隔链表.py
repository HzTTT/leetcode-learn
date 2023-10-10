#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 创建两个虚拟节点，用于存储小于x和大于等于x的节点
        dummy1 = ListNode()  # 存储小于x的节点
        dummy2 = ListNode()  # 存储大于等于x的节点
        p1, p2, p = dummy1, dummy2, head  # 初始化指针，p1指向dummy1，p2指向dummy2，p指向head

        while p:
            if p.val < x:
                p1.next = p  # 将小于x的节点连接到dummy1后
                p1 = p1.next  # 移动p1指针
            else:
                p2.next = p  # 将大于等于x的节点连接到dummy2后
                p2 = p2.next  # 移动p2指针

            temp = p.next  # 保存p的下一个节点
            p.next = None  # 断开p与下一个节点的连接
            p = temp  # 移动p指针到下一个节点

        p1.next = dummy2.next  # 将dummy2中的节点连接到dummy1的末尾
        return dummy1.next  # 返回dummy1的下一个节点作为新的头节点
# @lc code=end

