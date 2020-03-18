class Solution:
    def sumNums(self, n: int) -> int:
        def recursion(n):
            return n and n + recursion(n-1)
        return recursion(n)

if __name__ == "__main__":
    s = Solution()
    print(s.sumNums(15))