n=int(input())
def geo(n):
    if n == 1:
        return 1
    else:
        return (1/2**n) + (geo(n-1))
print(geo(n))


