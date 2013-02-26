import datetime
import math

n = int(raw_input('Enter number to get factors \n > '))

def factor(n):
    '''Find the factors of the number given by the user '''
    factors=[]
    try:
        for i in range(int(math.sqrt(n)),0,-1):     #Here you can import math, or do int(n**(0.5))
            if n%i==0:
        
                factors.append(i)   #first factor
                factors.append(n/i) #the factors counterpart
        
        print 'The factors of %d are...' % n
        factors = sorted(factors)
        print factors
    
    except MemoryError as k:
        print k

if __name__=='__main__':
    t1 = datetime.datetime.now()
    factor(n)
    t2 = datetime.datetime.now()
    dt=t2-t1

print "That took %d seconds and %d microseconds" % (dt.seconds, dt.microseconds)

