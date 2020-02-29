#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        def pathSum(root,sums):
            if not root.left and not root.right:
                sums -= root.val
                if sums == 0:
                    return True
            sums -= root.val
            flag = False
            if root.left:
                flag = pathSum(root.left,sums)
            if not flag and root.right:
                flag = pathSum(root.right,sums)
            return flag
        return pathSum(root,sum)

# @lc code=end
