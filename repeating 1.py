n=list(map(int, input().split()))
for i in range(0,len(n)):
    count=0
    for j in range(i,len(n)):
        if(n[i]==n[j]):
            count=count+1
    if(count==1):
        print(n[i])