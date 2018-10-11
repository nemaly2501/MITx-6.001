"""
Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.

"""



def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    a=[]
    b=list(aDict.values())
    c=[]
    for i in b:
      if(b.count(i)==1):
        c.append(i)
    for i in aDict.keys():
      if aDict[i] in c: 
        a.append(i)
    a.sort()
    return a
	
	
	
	