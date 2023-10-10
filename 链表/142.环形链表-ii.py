#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化快慢指针
        fast, slow = head, head
        
        # 判断链表是否有环
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # 有环的情况下，将慢指针重新指向头结点
                slow = head
                # 找到环的入口节点
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        
        # 没有环的情况下，返回None
        return None
        
# @lc code=end