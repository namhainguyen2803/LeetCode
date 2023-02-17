def submax(lis):
    n = len(lis)
    dp = [0]*n
    dp[0] = lis[0]
    for i in range(1,n):
        dp[i] = max(dp[i-1],0) + lis[i]
    return max(dp)
