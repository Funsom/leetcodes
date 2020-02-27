#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        i = 0
        while i + 1 < n:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                n -= 1
            else:
                i += 1
        return n     


# @lc code=end

