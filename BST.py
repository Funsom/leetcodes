# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:49:52 2020

@author: Illusion
"""

class treeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class BST():
    def __init__(self):
        self.root = None
        
    def preOrderTN(self):
        '''
        二叉树的前序遍历
        '''
        def preOrder(root):
            if not root: return
            print(root.val)
            if root.left:
                preOrder(root.left)
            if root.right:
                preOrder(root.right)
        preOrder(self.root)
    def inOrderTN(self):
        '''
        二叉树的中序遍历
        '''
        def inOrder(root):
            if not root: return
            
            if root.left:
                inOrder(root.left)
            print(root.val)
            if root.right:
                inOrder(root.right)
        inOrder(self.root)
    def addTreeNode(self,val):
        
        if not self.root:
            return treeNode(val)
        head = self.root
        while head:
            if val < head.val and not head.left :
                head.left = treeNode(val)
                break
            elif val > head.val and not head.right:
                head.right = treeNode(val)
                break
            elif val < head.val:
                head = head.left
            elif val > head.val:
                head = head.right
            elif head.val == val:
                break
        return self.root
    
    def buildBST(self,lists):
        self.root = treeNode(lists[0])
        for i in lists[1:]:
            self.addTreeNode(i)
        self.inOrderTN()
        
        
if __name__ == "__main__":
    bst = BST()
    bst.buildBST([5,3,6,7,1])


























