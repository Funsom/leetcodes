#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        def levelOrder(root):
            cur_layer = [root]
            res = []
            while cur_layer:
                temp = []
                next_layer = []
                for i in cur_layer:
                    temp.append(i.val)
                    if i.left:
                        next_layer.append(i.left)
                    
                    if i.right:
                        next_layer.append(i.right)

                res.append(temp)
                cur_layer = next_layer
            return res
        return levelOrder(root)[::-1]
# @lc code=end

