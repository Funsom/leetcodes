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
        if not root: return 0
        
        def depths(root,depth):
            nonlocal maxs,dep
            if not root.left and not root.right:
                depth += 1
                maxs = max(maxs,depth)
                dep.append(depth)
                return
            depth += 1
            if root.left:
                depths(root.left,depth)
            if root.right:
                depths(root.right,depth)
        maxs = 0
        dep = []
        depths(root,0)
        print(maxs,dep)
        return (maxs - min(dep)) <= 1
# @lc code=end

