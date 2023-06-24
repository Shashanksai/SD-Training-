#palindrome
n=int(input("Enter Number:"))
original_number=n
reverse=0
while original_number!=0:
    reverse=reverse*10+(original_number%10)
    original_number//=10
if reverse==n:
    print(n,"is a Palindrome")
else:
    print(n,"is not a Palindrome")
    
    