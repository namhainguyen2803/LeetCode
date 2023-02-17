from tkinter import N


def longpal(s):
    
    lis = []
    for i in range(len(s)):
        lis.append('|')
        lis.append(s[i])
    lis.append('|')
    n = len(lis)
    dp = [0]*n
    for center in range(len(lis)):
        radius = 0
        while center - radius >= 0 and center + radius < n:
            if lis[center-radius] == lis[center+radius]:
                radius += 1
            else:
                break
        dp[center] = radius - 1
    mx = max(dp)
    for stt,val in enumerate(dp):
        if mx == val:
            cen = stt
    ans = ""
    for i in range(cen - mx, cen + mx + 1):
        if lis[i].isalpha() and lis[i].isdigit():
            ans += lis[i]
        else:
            continue
    return (ans)
st = 'babad'
print(longpal(st))