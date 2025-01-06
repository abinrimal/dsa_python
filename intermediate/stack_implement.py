'''
Question: Implement a Stack using Lists
Description:
Implement a stack using Python lists. The stack should support the following operations:

push(x): Adds element x to the stack.
pop(): Removes the top element from the stack and returns it.
peek(): Returns the top element without removing it.
is_empty(): Returns True if the stack is empty, otherwise False.
size(): Returns the number of elements in the stack.  
LIFO
'''

arr = [54,23,23,12,65]
arr.append(12)
arr.pop()
print('Top Element is: ',arr[-1]) #peek the last element in the array
print(len(arr) == 0) # Is Empty check
print(len(arr)) # Size of stack check