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
        dummy1 = ListNode()
        dummy2 = ListNode()
        p1,p2,p = dummy1,dummy2,head

        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next

            temp = p.next
            p.next = None
            p = temp
        
        p1.next = dummy2.next

        return dummy1.next
# @lc code=end

