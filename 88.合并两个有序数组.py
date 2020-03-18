#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        na = len(nums1)
        curA = m - 1
        endA = na - 1
        curB = n - 1
        while curB >= 0 and curA >=0:
            if nums1[curA] < nums2[curB]:
                nums1[endA] = nums2[curB]
                endA -= 1
                curB -= 1
            else:
                nums1[endA] = nums1[curA]
                nums1[curA] = 0
                endA -= 1
                curA -= 1
        if endA != -1 and curB != -1 :
            nums1[:endA+1] = nums2[:curB+1]
        # elif endA == 0 and curB == 0:
        #     nums1[endA] = nums2[curB]


# if __name__ == "__main__":
#     s = Solution()
#     list1 = [1,0]#[1,2,3,0,0,0]
#     list2 = [0]
#     s.merge(list1,1,list2,0)
#     #print(list1)


# @lc code=end

