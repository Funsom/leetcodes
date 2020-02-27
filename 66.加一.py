#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        R = n - 1
        up = 0
        if digits[R] + 1 > 9:
            digits[R] = 0
            up = 1
            R -= 1
        else:
            digits[R] += 1
            return digits
        while R >= 0:
            if up + digits[R]> 9:
                digits[R] = 0
                up = 1
            else:
                digits[R] += up
                return digits
            R -= 1
        return [1] + digits


# @lc code=end

