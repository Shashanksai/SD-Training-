'''print the following output:
*
**
***	'''
n=int(input("Enter Number of lines:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")