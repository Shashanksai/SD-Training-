'''print the follwing output:
a
bb
ccc	'''
n=int(input("Enter Number of lines:"))
a=*
for i in range(n):
    for j in range(i+1):
        print(chr(a),end=' ')
    print('\n')
    a+=1