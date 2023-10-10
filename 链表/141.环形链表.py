#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 初始化快慢指针
        fast, slow = head, head
        
        # 当快指针和快指针的下一个节点都存在时，进行循环
        while fast and fast.next:
            # 快指针每次移动两步
            fast = fast.next.next
            # 慢指针每次移动一步
            slow = slow.next
            
            # 如果快指针和慢指针相遇，则表示链表有环
            if fast == slow:
                return True
        
        # 如果循环结束仍未找到环，则表示链表无环
        return False
# @lc code=end
