mainlist=[]
st=int(input("enter the list capacity"))
for i in range(st):
    elements=int(input("enter the item"))
    if(elements%10==7):
        mainlist.append(elements)
print(mainlist)

    