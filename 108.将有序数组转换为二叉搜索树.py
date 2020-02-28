#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bulidTree(lists):
            if not lists: return
            n = len(lists)
            median = n >> 1
            root = TreeNode(lists[median])
            root.left = bulidTree(lists[:median])
            root.right = bulidTree(lists[median+1:])
            return root
        return bulidTree(nums)


# @lc code=end

