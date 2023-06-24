'''print the follwing output:
abc
ab
a	'''
n=int(input("Enter Number of lines:"))
for i in range(n):
    asci=97
    for j in range(n,i,-1):
        print(chr(asci),end=' ')
        asci+=1
    print('\n')