#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:return []
        m = len(matrix)
        n = len(matrix[0])
        c = 0
        mins = min(n,m)
        div, mod = divmod(mins,2)
        count = div + mod
        res = []
        while c < count:
            res.extend(matrix[c][c:n-c])
            #print(1,res)
            for i in range(c+1,m-c):
                res.append(matrix[i][n-c-1])
            #print(2,res)
            temp = []
            if m - c - 1 > c and n - c - 1 > c: 
                for i in range(c,n-c-1):
                    temp.append(matrix[m-c-1][i])
                
                res.extend(temp[::-1])
                #print(3,res)    
                temp = []
                for i in range(c+1,m-c-1):
                    temp.append(matrix[i][c])
                res.extend(temp[::-1])
                #print(4,res) 
            c += 1
            
        return res

# if __name__ == "__main__":
#     s = Solution()
#     matrix = [[]]
#     print(s.spiralOrder(matrix))



# @lc code=end

