n,b=int(input()),int(input())
c=n>>b
'''n=(bin(n))#bin converts int to binary and store it in string format
if b>=len(n):
    print("False")
elif n[len(n)-(b+1)]=='1':
    print("True")
else:
    print("False")'''
if c%2==0:
    print("False")
else:
    print("True")
'''
d=bin(c)
if(d[-1]=='1'):
    print("True")
else:
    print("False")
    '''