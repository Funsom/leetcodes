#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
         
        def rebulit(inorder,preorder):
            if not inorder: return
            n = len(inorder)
            dic = {}
            for i in range(n):
                dic[inorder[i]] = i
            
            root = TreeNode(preorder[0])
            index = dic[preorder[0]]
            root.left = rebulit(inorder[:index],preorder[1:index+1])
            root.right = rebulit(inorder[index+1:],preorder[index+1:])
            return root           
        return rebulit(inorder,preorder)



# @lc code=end

