'''print the following output
1
1
123	'''
n=int(input("Enter Number of lines:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print('\n')