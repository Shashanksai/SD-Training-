n=int(input("Enter the Numbers"))
l=list(map(int,input().split()))
unq=5

count=0
for i in l:
    if(i<unq):
        count+=1
if(count==unq):
    print("unique")
else:
    print("not unique")
