'''
Implement a Queue using Lists
Description:
Implement a queue using Python lists. A queue follows the FIFO (First In, First Out) principle, meaning the first element added is the first one to be removed.

The queue should support the following operations:
enqueue(x): Adds element x to the end of the queue.
dequeue(): Removes and returns the element at the front of the queue.
peek(): Returns the element at the front of the queue without removing it.
is_empty(): Returns True if the queue is empty, otherwise False.
size(): Returns the number of elements in the queue.

'''

arr = [54,23,23,12,65]
arr.append(12) # Enqueues element
print(arr.pop(0) ) # dequeus
print('Top Element is: ',arr[0]) #peek the last element in the array
print(len(arr) == 0) # Is Empty check
print(len(arr)) # Size of queue check


