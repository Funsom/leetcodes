class Solution:
    def findContinuousSequence(self, target: int):
        import math
        res = []
        n = math.ceil((math.sqrt(9 + 8 * target)-3)/2)
        for i in range(2,n+1):
            temp = target - i*(i+1)//2
            if temp % i == 0:
                a = target // i - (i+1)//2
                ans = [a + j for j in range(1,i+1)]
                res.insert(0,ans)
        return res

if __name__ == "__main__":
    s = Solution()
    ans = s.findContinuousSequence(5)
    print(ans)