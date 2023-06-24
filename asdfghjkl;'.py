a=list(map(int, input().split()))
count = 0
for i in range(0,len(a),1):
    c=c^a[i]
    print(c)