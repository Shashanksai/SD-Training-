def LCM(x,y):
    z=x%y
    if (z==0):
        return x
    else:
        return x*LCM(y,x)/z
x=int(input("enter num1"))
y=int(input("enter num2"))
print(LCM(x,y))

