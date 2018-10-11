'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''

ma=0
start=0
end=0
ch=''
c=0
for i in range (0,len(s)-1):
    if (s[i]>s[i+1]):
        end=i
        if ma<(end-start+1):
            ch=s[start:end+1]
            ma=end-start+1
        start=i+1
    else: end=i
end+=1
if ma<(end-start+1):
            ch=s[start:end+1]
print("Longest substring in alphabetical order is: "+ch)