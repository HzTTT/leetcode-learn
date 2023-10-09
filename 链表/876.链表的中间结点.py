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
        if not head:
            return None
        fast,slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

# @lc code=end

