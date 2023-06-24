# function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

# function to check if a number is a Krishnamurthy number
def isKrishnamurthy(num):
    # calculate the sum of the factorial of each digit in the number
    digit_sum = sum(factorial(int(digit)) for digit in str(num))
    
    # check if the sum is equal to the original number
    if digit_sum == num:
        return True
    else:
        return False

# example usage
num =int(input("Enter Number:"))
if isKrishnamurthy(num):
    print(num, "is a Krishnamurthy number")
else:
    print(num, "is not a Krishnamurthy number")
