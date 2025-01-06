#Write a function that takes an array as input and returns the array in reverse order.

def reverse_arr(arr):
    return arr[::-1]   #Reverse an array using slicing.

#or
def reverse_arr2(arr):
    return arr[-1::-1] #explicit slicing that starts from the last element and steps backward.


try:
    n = int(input('Enter number of elements to reverse: '))
    if n <= 0:
        print("Array size must be greater than 0.")
    else:
        arr = []
        for i in range(n):
            x = input(f'Enter element {i+1}: ')
            arr.append(x)

        print('Original array:', arr)
        print('Reversed array:', reverse_arr(arr))

except ValueError:
    print("Invalid input. Please enter a valid integer.")  # Handle invalid input. 


