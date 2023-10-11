#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        if not root:
            return []
        list.append(root.val)
        list.extend(self.preorderTraversal(root.left))
        list.extend(self.preorderTraversal(root.right))

        return list
 
# @lc code=end

