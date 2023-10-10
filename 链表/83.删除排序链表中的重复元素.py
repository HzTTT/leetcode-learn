#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果头节点为空，则直接返回空
        if not head:
            return head
        
        # 初始化快慢指针为头节点
        slow, fast = head, head
        
        # 遍历链表
        while fast:
            # 如果慢指针的值不等于快指针的值
            if slow.val != fast.val:
                # 将慢指针的下一个节点指向快指针
                slow.next = fast
                # 慢指针向后移动一位
                slow = slow.next
            # 快指针向后移动一位
            fast = fast.next
        
        # 将慢指针的下一个节点设为None
        slow.next = None
        
        # 返回头节点
        return head
# @lc code=end
