class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        res = m * n
        for i in range(m):
            for j in range(n):
                s1 = str(i)
                s2 = str(j)
                sums = 0
                
                for a in s1 + s2:
                    sums += int(a)
                print(s1+s2,sums)
                if sums > k:
                    res -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(16,8,4))