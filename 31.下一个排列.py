#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
# public void nextPermutation(int[] nums) {
#         int i = nums.length - 2;
#         while (i >= 0 && nums[i + 1] <= nums[i]) {
#             i--;
#         }
#         if (i >= 0) {
#             int j = nums.length - 1;
#             while (j >= 0 && nums[j] <= nums[i]) {
#                 j--;
#             }
#             swap(nums, i, j);
#         }
#         reverse(nums, i + 1);
#     }

#     private void reverse(int[] nums, int start) {
#         int i = start, j = nums.length - 1;
#         while (i < j) {
#             swap(nums, i, j);
#             i++;
#             j--;
#         }
#     }

#     private void swap(int[] nums, int i, int j) {
#         int temp = nums[i];
#         nums[i] = nums[j];
#         nums[j] = temp;
#     }
# }



class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:return
        n = len(nums)
        if n==1:return
        i = n - 2
        j = 0
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i == -1: nums.sort()
        else:
            j = n-1
            while j >= 0  and nums[j] <= nums[i]:
                j = j - 1
            nums[i],nums[j] = nums[j],nums[i]
            
            nums[i+1:] = sorted(nums[i+1:])
        print(nums)


if __name__ == "__main__":
    s = Solution()
    s.nextPermutation([5,1,1])




# @lc code=end

