#Prime Number
n=int(input("Enter Number:"))
rev=0
g_n=0
h=0
for i in range(2,n):
    if (n%i==0):
        print(n,"is not Prime Number")
        h=1
        break
if (h==0 or):
    print(n,"is a Prime Number")