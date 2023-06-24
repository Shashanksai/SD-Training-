'''print the following output:
a b c
 a b
  c	'''
n=int(input("Enter Number of lines:"))
for i in range(n):
    asci=97
    space=0
    while space!=i:
        print(' ',end='')
        space+=1
    for j in range(n,i,-1):
        print(chr(asci),end=" ")
        asci+=1
    print("\n")