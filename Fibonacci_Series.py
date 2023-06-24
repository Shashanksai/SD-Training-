#Fibonacci Series
n=int(input("Enter Series Length:"))
a,b=0,1
print(a,b,end=" ")
for i in range(n-2):
    c=b
    b=a+b
    a=c
    print(b,end=" ")