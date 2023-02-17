def divisorGame(n):
    choose = list()
    dp = [None] * (n + 1)
    dp[1] = False
    dp[2] = True
    for i in range(2,n+2):
        for j in range(1,i):
            if i % j == 0 and i + j < n + 1:
                if dp[i] == False:
                    dp[i+j] = True
                elif dp[i] == True:
                    if dp[i+j] == None:
                        dp[i+j] = False
                    elif dp[i+j] == False:
                        dp[i+j] = False
                    elif dp[i+j] == True:
                        dp[i+j] = True
    return dp

print(divisorGame(10))