a=[0,-1,2,-3,1]
b=int(input())
c=0
for i in range(0,len(a),1):
    for j in range(i+1,len(a),1):
        if(a[i]+a[j]==b):
            c=c+1
if(c!=0):
    print("Yes")
else:
    print("NO")