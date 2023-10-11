#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # 用于存储最大深度
        self.depth = 0  # 用于存储当前深度
        self.traverse(root)  # 调用辅助函数进行遍历
        return self.res  # 返回最大深度

    def traverse(self, root: Optional[TreeNode]):
        if not root:
            return  # 如果节点为空，返回

        self.depth += 1  # 增加当前深度

        if not root.left and not root.right:  # 如果节点没有左子树和右子树，说明到达叶节点
            self.res = max(self.res, self.depth)  # 更新最大深度

        self.traverse(root.left)  # 递归遍历左子树
        self.traverse(root.right)  # 递归遍历右子树

        self.depth -= 1  # 返回上一节点，减少当前深度

        return  # 返回

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # 如果节点为空，返回0

        left = self.maxDepth(root.left)  # 递归计算左子树的最大深度
        right = self.maxDepth(root.right)  # 递归计算右子树的最大深度

        return max(left, right) + 1  # 返回左右子树中较大的深度加1