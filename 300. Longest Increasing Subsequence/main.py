def LIS(lis):
    if len(lis)==1:
        return 1
    else:
        dp = [1]*len(lis)
        for i in range(len(lis)):
            for j in range(i):
                if lis[i]>lis[j]:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)
lis = [10,9,2,5,3,7,101,18]
print(LIS(lis))