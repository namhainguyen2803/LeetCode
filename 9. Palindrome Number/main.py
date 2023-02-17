def pal(x):
    if str(x) == str(x)[::-1]:
        return True
    return False
print(pal(12221))