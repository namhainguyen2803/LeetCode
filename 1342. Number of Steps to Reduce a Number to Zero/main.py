def counting(n,num=0):
    if n==0:
        return num
    else:
        if n%2==0:
            return counting(n/2,num=num+1)
        else:
            return counting(n-1,num=num+1)
print(counting(14))