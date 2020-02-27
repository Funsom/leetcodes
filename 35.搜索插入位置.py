#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if not nums: return 0
        n = len(nums)
        L = 0
        R = n - 1
        while L <= R: # 一定记住 tricky
            
            mid = L + (R - L) // 2
            print(L,mid,R)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                R = mid - 1
            else:
                L = mid + 1
        return L 
'''
s = Solution()
print(s.searchInsert([1,3,5,6],2))            
'''

# @lc code=end

