#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s // 3
        n, i, cur = len(A), 0, 0
        while i < n:
            cur += A[i]
            if cur == target:
                break
            i += 1
        if cur != target:
            return False
        j = i + 1
        while j + 1 < n:  # 需要满足最后一个数组非空
            cur += A[j]
            if cur == target * 2:
                return True
            j += 1
        return False


if __name__ == "__main__":
    s = Solution()
    A = [18,12,-18,18,-19,-1,10,10]
    res = s.canThreePartsEqualSum(A)
    print(res)
# @lc code=end

