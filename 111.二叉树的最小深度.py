#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        def depth(root,depths):
            if not root.left and not root.right:
                return depths
            if root.left:

                leftDepths = depth(root.left,depths + 1) 
            if root.right:
                rightDepths = depth(root.right,depths + 1)
            if root.left and root.right:
                return min(leftDepths,rightDepths)
            elif not root.left:
                return rightDepths
            else:
                return leftDepths
        return depth(root,1)
# @lc code=end

