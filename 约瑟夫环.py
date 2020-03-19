def func(n,m,id):
    dp = [0 for _ in range(id+1)]
    for i in range(2,id+1):
        dp[i] = (dp[i-1]+m) % i
    print(dp[1:])
if __name__ == "__main__":
    func(60,3,23)