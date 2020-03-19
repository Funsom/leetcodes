#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        if not rec1 or not rec2: return False
        x1,y1,x2,y2 = rec1
        m1,n1,m2,n2 = rec2
        if m1 < x2 and n1 < y2 and m1 > x1 and n1 > y1:
            return True
        if x1 < m2 and y1 < n2 and x1 > m1 and y1 > n1:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    rec1 = [7,8,13,15]
    rec2 = [10,8,12,20]
    res = s.isRectangleOverlap(rec1,rec2)
    print(res)

# @lc code=end

