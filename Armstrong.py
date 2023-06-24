#Armstrong
n=input("Enter Number:")
exponent=len(n)
n=int(n)
result=0
original_number=n
while original_number!=0:
    digit=original_number%10
    result+=digit**exponent
    original_number//=10
if result==n:
    print(n,"is an Armstrong")
else:
    print(n,"is not an Armstrong")