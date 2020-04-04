#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#

# @lc code=start
class Solution:
    def maxDistance(self, grid) -> int:
        n = len(grid)
        queue = []
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    queue.append((row,col))
        while queue:
            next_queue = []
            for q in queue:
                i,j = q
                if i-1 >= 0 and grid[i-1][j] == 0:
                    grid[i-1][j] = grid[i][j] + 1 
                    next_queue.append((i-1,j))
                if i+1 <= n-1 and grid[i+1][j] == 0:
                    grid[i+1][j] = grid[i][j] + 1 
                    next_queue.append((i+1,j))
                if j-1 >= 0 and grid[i][j-1] == 0:
                    grid[i][j-1] = grid[i][j] + 1 
                    next_queue.append((i,j-1))
                if j+1 <= n-1 and grid[i][j+1] == 0:
                    grid[i][j+1] = grid[i][j] + 1 
                    next_queue.append((i,j+1))
            queue = next_queue
        print(grid)
        ans = max([max(i) for i in grid])
        return ans - 1 if ans - 1 > 0 else -1 

if __name__ == "__main__":
    s = Solution()
    grid = [[1,0],[0,0]]
    res = s.maxDistance(grid)
    print(res)
        
# @lc code=end

