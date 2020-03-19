#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        import math
        res = [0 for _ in range(num_people)]
        count =  int((math.sqrt(candies*8-3)-1)/2)
        sums = count*(count+1)//2
        charge = candies - sums
        div,mod = divmod(count,num_people)
        for i in range(num_people):
            if i < mod:
                res[i] = (div+1)*(i+1) + num_people*(div*(div+1))//2
            else:
                res[i] = div*(i+1) + num_people*(div*(div-1))//2
        res[mod] += charge
        return res


# if __name__ == "__main__":
#     s = Solution()
#     res = s.distributeCandies(100,5)
#     print(res)
# @lc code=end

