def minimumCost(cost):
    n = len(cost)
    # declare an array
    dp = [0]*n
 
    # base case
    if n == 1:
        return cost[0]
 
    # initially to climb
    # till 0-th or 1th stair
    dp[0] = cost[0]
    dp[1] = cost[1]
 
    # iterate for finding the cost
    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
 
    # return the minimum
    return min(dp[n - 2], dp[n - 1])
print(minimumCost([10,15,20]))