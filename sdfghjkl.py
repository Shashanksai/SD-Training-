def is_perfect(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    if sum(divisors) == number:
        return True
    else:
        return False

# Example usage
'''number = 6
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")'''
