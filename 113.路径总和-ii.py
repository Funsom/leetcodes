#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def pathSum(self, root, sum: int):
        if not root: return []
        def paths(root,sums,path):
            if not root.left and not root.right:
                sums -= root.val
                path.append(root.val)
                if sums == 0:
                    res.append(copy.copy(path))
                return

            path.append(root.val)
            sums -= root.val
            if root.left:
                paths(root.left,sums,path)
                path.pop()
            if root.right:
                paths(root.right,sums,path)
                path.pop()
        res = []
        paths(root,sum,[])
        return res
# @lc code=end

