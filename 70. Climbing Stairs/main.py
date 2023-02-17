def climbing(n,sto = {}):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    if n in sto:
        return sto[n]
    else:
        sto[n] = climbing(n-1,sto) + climbing(n-2,sto)
        return sto[n]
print(climbing(3))