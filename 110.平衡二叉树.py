#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root: return 0
            left = depth(root.left)
            if left == -1:return -1
            right = depth(root.right)
            if right == -1: return -1
            return max(left,right) + 1 if abs(left - right) < 2 else -1
        return depth(root) != -1
# @lc code=end

