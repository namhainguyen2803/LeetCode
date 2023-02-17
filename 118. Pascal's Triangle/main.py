sto=[[],[1],[1,1]]
def pascal(n):
    global sto
    if len(sto)>=n+1:
        return sto[n]
    if n == 1:
        return sto[1]
    elif n==2:
        return sto[2]
    else:
        lis = [0]*n
        lis[0] = 1
        lis[-1] = 1
        lis_prev = pascal(n-1)
        for i in range(1,len(lis)-1):
            lis[i] = lis_prev[i-1] + lis_prev[i]
        sto.append(lis)
        return sto[n]
x = pascal(5)
print(sto[1:])



















'''
        def pascal(n,sto=[[],[1],[1,1]]):
            if n == 1:
                return sto[1]
            elif n==2:
                return sto[2]
            else:
                lis = [0]*n
                lis[0] = 1
                lis[-1] = 1
                lis_prev = pascal(n-1,sto)
                for i in range(1,len(lis)-1):
                    lis[i] = lis_prev[i-1] + lis_prev[i]
                sto.append(lis)
                return lis
        sto = []
        for i in range(numRows):
            sto.append(pascal(i))
        return sto'''