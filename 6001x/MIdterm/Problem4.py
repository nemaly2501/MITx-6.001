"""
Problem 4
15.0/15.0 points (graded)
Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings. Your function should not modify aList.
"""


def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    b=[]
    for a in aList:
        if len(a)<4:
            b.append(a)
    return b