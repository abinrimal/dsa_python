#Question: Find the Maximum and Minimum in an Array
#Problem Statement: Given an array of integers, find the maximum and minimum values in the array.

def find_max_min(arr):
    if not arr:
        raise ValueError("The array is empty!")
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    return max_val, min_val

 
arr = [12, 45, 7, 23, 56, 89,]
max_val, min_val = find_max_min(arr)
print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
