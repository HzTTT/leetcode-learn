#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果头节点为空，则返回None
        if not head:
            return None
        
        # 定义快慢指针，初始值为头节点
        fast, slow = head, head
        
        # 当快指针和快指针的下一个节点都存在时，快指针走两步，慢指针走一步
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 返回慢指针所在的节点
        return slow
# @lc code=end
