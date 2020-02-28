#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 堆栈层序遍历
        if not p or not q : return p == q
        def levelOrder(root):
            cur_layer = [root]
            res = []
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
                
                res.extend(temp)
                cur_layer = next_layer
            return res
                
        levelOrderResP = levelOrder(p)
        levelOrderResQ = levelOrder(q)
        '''
        if len(levelOrderResP) != len(levelOrderResQ):
            return False
        n = len(levelOrderResP)
        for i in range(n):
            if levelOrderResP[i] != levelOrderResQ[i]:
                return False
        
        return True
        '''
        return levelOrderResP == levelOrderResQ
# @lc code=end

