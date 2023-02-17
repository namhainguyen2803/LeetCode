def minpath(lis):
    dp = [[0 for i in range(len(lis[0]))] for j in range(len(lis))]
    col = len(dp[0])
    row = len(dp)
    #dp[0][0] = lis[0][0]
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                dp[i][j] = lis[i][j]
            if i ==0:
                dp[i][j] = dp[i][j-1] + lis[i][j]
            elif j==0:
                dp[i][j] = dp[i-1][j] + lis[i][j]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + lis[i][j]
    return min(dp[row-2][col-1],dp[row-1][col-2]) + lis[row-1][col-1]
#grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
print(minpath(lis=grid))
            
            