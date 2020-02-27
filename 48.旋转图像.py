#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # (0,i)    ->  (i,n-1)
        # (i,n-1)  ->  (n-1,n-i-1)
        # (n-1,n-i-1) -> (n-i-1,0)
        # (n-i-1,0) -> (0,i)
        n = len(matrix)
        for i in range(n//2 + n % 2 ):
            for j in range(n//2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


# @lc code=end

