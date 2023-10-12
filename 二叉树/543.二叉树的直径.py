#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        self.maxDiameter = max(self.maxDiameter, left+right)

        return 1 + max(right,left)
        
# @lc code=end

