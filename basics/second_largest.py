#Write a function to find the second largest element in an array. 
# If the array has fewer than two unique elements, return None.

def second_largest(arr):
    if len(set(arr)) < 2:  # Check if there are fewer than 2 unique elements
        return None
    max_num = max(arr)
    second_max = min(arr)

    for num in arr:
        if num != max_num and num > second_max:
            second_max = num 
    return second_max


arr = [21,43,1,21,40,12]
print (second_largest(arr))
