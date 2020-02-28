#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def levelOrder(root):
            cur_layer = [root]
            while cur_layer:
                temp = []
                next_layer = []
                for i in cur_layer:
                    if not i:
                        temp.append(None)
                    else:
                        temp.append(i.val)
                        if i.left:
                            next_layer.append(i.left)
                        else:
                            next_layer.append(None)
                        if i.right:
                            next_layer.append(i.right)
                        else:
                            next_layer.append(None)
                n = len(temp)
                L, R = 0,n-1
                while L < R:
                    if temp[L] != temp[R]:
                        return False
                    else:
                        L += 1
                        R -= 1
                cur_layer = next_layer
            return True
                
        return levelOrder(root)
# @lc code=end

