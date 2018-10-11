'''
Problem 6
0.0/20.0 points (graded)
Implement a function that meets the specifications below.

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
For example,

max_val((5, (1,2), [[1],[2]])) returns 5.
max_val((5, (1,2), [[1],[9]])) returns 9.

'''


def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
    for i in t:
      if (isinstance(i, int)):
        m=max(m,i)
      else:
        m=max_val(i,m)
    return (m)	