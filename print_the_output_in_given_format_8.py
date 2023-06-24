'''print the following output:
* * * 
 * *
  *	'''
n=int(input("Enter Number of lines:"))
for i in range(n):
    space=0
    for j in range(n,i,-1):
        while space!=i:
            print("*",end='')
            space+=1
        print(" ",end=" ")
    print("\n")
