#Question: Check if a String is a Palindrome
#A palindrome is a string that reads the same backwards as forwards. For example, "madam is a palindrome.
#Write a function that takes a string as input and returns True if the string is a palindrome,
#and False otherwise.

def check_palindrome(word):
    cleaned_word = word.lower() # convert to lowercase
    reversed_word = cleaned_word[::-1]
    return cleaned_word == reversed_word 

word = input("Please enter a word: ")
print(check_palindrome(word))