def pal(cost):
    n = len(cost) + 1
    minCost = [0] * (n)
    for i in range(2, n):
        oneStep = minCost[i-1] + cost[i-1]
        twoStep = minCost[i-2] + cost[i-2]
        minCost[i] = min(oneStep, twoStep)
    return minCost[n-1]
    
print(pal([10,15,20]))