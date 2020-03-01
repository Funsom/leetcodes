#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return 
        n = len(numbers)
        L, R = 0, n-1
        while L < R:
            sums = numbers[L] + numbers[R]
            if sums == target:
                return [L+1,R+1]
            elif sums > target:
                R -= 1
            else:
                L += 1


# @lc code=end
