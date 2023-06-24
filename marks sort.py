n=int(input("Enter the total students"))
marks=list(map(int,input().split()))
k=int(input("Enter Expected Students"))
marks.sort()
sum=0
for i in range(k):
    sum+=marks[k]
if(sum<25):
    print("average")
else:
    print("good")
