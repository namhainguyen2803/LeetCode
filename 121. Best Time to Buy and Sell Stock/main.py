def Profit(lis):
    profit = [0]*len(lis)
    lowest = 10000
    for i in range(len(lis)):
        if lowest > lis[i]:
            lowest = lis[i]
        profit[i] = max(profit[i],lis[i]-lowest)
    return max(profit)
prices = [7,1,5,3,6,4]
print(Profit(prices))
'''
        def Profit(lis):
            profit = [0]*len(lis)
            for i in range(len(lis)):
                for j in range(0,i+1):
                    profit[i] = max(profit[i],lis[i]-lis[j])
            return max(profit)
        return Profit(prices)'''