#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
'''
public class Solution {
    public Node construct(int[][] grid) {
        return construct(grid, 0, grid.length - 1, 0, grid.length - 1);
    }

    private Node construct(int[][] grid, int top, int bottom, int left, int right) {
        for (int i = top; i <= bottom; i++) {
            for (int j = left; j <= right; j++) {
                if (grid[i][j] != grid[top][left]) {
                    Node node = new Node(false, false);
                    int mid1 = top + ((bottom - top) >> 1), mid2 = left + ((right - left) >> 1);
                    node.topLeft = construct(grid, top, mid1, left, mid2);
                    node.topRight = construct(grid, top, mid1, mid2 + 1, right);
                    node.bottomLeft = construct(grid, mid1 + 1, bottom, left, mid2);
                    node.bottomRight = construct(grid, mid1 + 1, bottom, mid2 + 1, right);
                    return node;
                }
            }
        }
        return new Node(grid[top][left] == 1, true);
    }
}


'''


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def construct(grid,top,bottom,left,right):
            for i in range(top,bottom+1):
                for j in range(left,right+1):
                    if grid[i][j] != grid[top][left]:
                        node = Node(False,False)
                        mid1 = top + (bottom - top) // 2
                        mid2 = left + (right - left) // 2
                        node.topLeft = construct(grid,top,mid1,left,mid2)
                        node.topRight = construct(grid,top,mid1,mid2+1,right)
                        node.bottomLeft = construct(grid,mid1+1,bottom,left,mid2)
                        node.bottomRight = construct(grid,mid1+1,bottom,mid2+1,right)
                        return node
            return Node(grid[top][left] is 1,True)
        return construct(grid,0,len(grid)-1,0,len(grid[0])-1)


        
# @lc code=end

