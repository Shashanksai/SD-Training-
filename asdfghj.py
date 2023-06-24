def find_non_repeating(arr):
    xor_all = 0
    for i in range(len(arr)):
        xor_all ^= arr[i]
        
    xor_1_to_n = 0
    for i in range(1, len(arr) + 1):
        xor_1_to_n ^= i
        
    return xor_all ^ xor_1_to_n

arr = [2, 2, 3,99, 4, 5, 6, 7, 8, 9, 10, 10]
print(find_non_repeating(arr))

