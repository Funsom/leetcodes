#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 层序遍历
        if not root: return 0
        cur_layer = [root]
        res = 0
        while cur_layer:
            res += 1
            next_layer = []
            for i in cur_layer:
                if i.left:
                    next_layer.append(i.left)
                if i.right:
                    next_layer.append(i.right)
            cur_layer = next_layer
        return res



# @lc code=end

