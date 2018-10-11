'''
Exercise: genPrimes
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 10 minutes

Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
'''
	
def genPrimes():
    l = [2,3]
    yield l[0]
    yield l[1]
    n = 5           
    while True:
        c=0
        for i in l:
            if (n%i)==0:
                n+=2
                c=1
                break
        if c==0:
            l.append(n)
            yield l[-1]	