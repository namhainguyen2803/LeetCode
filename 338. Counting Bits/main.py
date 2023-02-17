sto = {}
def countBit(n):
    global sto
    if n in sto:
        return sto[n]
    if n==0:
        sto[n] = '0'
        return '0'
    elif n==1:
        sto[n] = '1'
        return '1'
    else:
        if n%2==0:
            sto[n] = countBit(n/2) + '0'
        else:
            sto[n] = countBit(n//2) + '1'
        return sto[n]
n = int(input())
for i in range(n+1):
    x = countBit(i)
print(sto)
res = []
for k in sto.values():
    res.append(k.count('1'))
print(res)