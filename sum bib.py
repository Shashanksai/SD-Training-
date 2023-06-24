a=list(map(int,input().split()))
s=int(input())
d={}
x=0
for i in range(len(a)):
    d[i]=a[i]
j=0
for i in range(a):
    if s-a[i] in d.values():
        print(true)
        x=1
        break
if x==0:
        print(false)
    