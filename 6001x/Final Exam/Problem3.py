"""
Problem 3
10.0/10.0 points (graded)
Write a Python function that takes in a string and prints out a version of this string that does not contain any vowels, according to the specification below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels will print Ths s grt!. If s = "a" then print_without_vowels will print the empty string .

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
"""
# Paste your function here
def print_without_vowels(s):
    ans=""
    for l in s:
        if l not in 'aAeEiIoOuU':
            ans+=l
    print(ans)            	