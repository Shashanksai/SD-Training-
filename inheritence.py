class fruit:
    def magical_prime(self):
        n=int(input("Enter Number:"))
        for i in range(2,n):
            if(n%i==0):
                print("Not magical prime")
                h=1
                break
        rev=0
        h=0
        while n!=0:
            rev=(rev*10)+(n%10)
            n//=10
        for i in range(2,rev):
            if(rev%i==0):
                print("Not Magical Prime")
                h=1
                break
        if(h==0):
            print("Magical Prime")
class apple(fruit):
    def neon(self):
            for i in range(100):
                n,result=i*i,0
                while n!=0:
                    result+=(n%10)
                    n=n//10
                if result==i:
                    print(i,"is Neon number")
class banana(apple):
    def pattern(self):
        n=input("Enter String:")
        for i in range(len(n)):
            for j in range(2*len(n)):
                if((i==j) or (i+j==(2*len(n))-2)):
                    print(n[i],end='')
                else:
                    print(" ",end='')
        print('')
class pineapple(banana):
    def addnum(self):
        #divide strings into character and numbers
        s=input("Enter String:")
        for i in s:
            if((i>=chr(97) and i<=chr(122)) or (i>=chr(65) and i<=chr(90))):
                print(i,end='')
        print("")
        for i in s:
            if((i>=chr(48) and i<=chr(57)) or i=='-'):
                print(i,end='')
#divide strnigs into character and convert the given number into single number
        s=input("\nEnter String:")
        for i in s:
            if((i>=chr(97) and i<=chr(122)) or (i>=chr(65) and i<=chr(90))):
                print(i,end='')
        print("")
        result=0
        for i in range(len(s)):
            if(s[i]=='-' and len(s)>i+1 and (s[i+1]>=chr(48) and s[i+1]<=chr(57))):
                n=int(s[i+1])
                result=result+(n*(-1))
            elif(s[i-1]!='-' and (s[i]>=chr(48) and s[i]<=chr(57))):
                result+=int(s[i])
        su,n=0,0
        if result<0:
            result*=-1
            n=1
        while result!=0:
            su=su+(result%10)
            result=result//10
        if n==0:
            print(su)
        else:
            print(su*-1)
f=pineapple()
f.magical_prime()
f.neon()
f.pattern()
f.addnum()