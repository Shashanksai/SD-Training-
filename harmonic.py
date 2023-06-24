n=int(input())
def harm(n):
    if n == 1:
        return 1
    else:
        return (1/n) + (harm(n-1))
print(harm(n))

