"""
Problem 4
15.0/15.0 points (graded)
Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order. A prime number is a number that is divisible only by 1 and itself. This function takes in an integer and returns a list of integers.

def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    # Your code here
    
"""
def primes_list(n):
    '''
    N: an integer
    '''
    # Your code here
    plist=[2]
    for i in range (3,n+1,2):
      flag=0
      j=3
      while j*j<=i:
        if (i%j)==0:
          flag=1
          break
        j+=1
      if flag==0:
        plist.append(i)
    return plist	