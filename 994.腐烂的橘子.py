#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid) -> int:
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        rot = []
        fresh = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rot.append((i,j))
                elif grid[i][j] == 1:
                    fresh.add((i,j))
        count = 0
        while fresh:
            new_rot = []
            while rot:
                x,y = rot.pop(0)
                if (x-1,y) in fresh:
                    fresh.remove((x-1,y))
                    new_rot.append((x-1,y))
                if (x+1,y) in fresh:
                    fresh.remove((x+1,y))
                    new_rot.append((x+1,y))
                if (x,y-1) in fresh:
                    fresh.remove((x,y-1))
                    new_rot.append((x,y-1))
                if (x,y+1) in fresh:
                    fresh.remove((x,y+1))
                    new_rot.append((x,y+1))
            rot = new_rot
            if not new_rot:
                break
            count += 1
        
        return count if not fresh else -1

if __name__ == "__main__":
    s = Solution()
    #grid = [[2,1,1],[1,1,0],[0,1,1]]
    grid = [[0,2]]
    print(s.orangesRotting(grid))

# @lc code=end

