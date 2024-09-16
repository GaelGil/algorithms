import sys
MAX_SIZE = 1_000_000

# the problem with recursion in python
# is that there is a recursion limit (1000 by default)
# if you want to compute higher fibonacci number
# then it is necessary to manually reset the recursion limit to some really big number
sys.setrecursionlimit(MAX_SIZE)

# create a big array to store values of fibonacci numbers
# initiate the array with -1
FIBO = [-1 for i in range(MAX_SIZE)]

def fib(n):
    if n >= 3:
        # if we have never computed the value of fib(n)
        # then store it to the array before returning it
        if FIBO[n] == -1:  
            FIBO[n] = fib(n-1) + fib(n-2)
        # if we already know the value of fib(n)
        # there is no need to calculate it all over again
    else:
        FIBO[n] = 1
    return FIBO[n]



print(fib(0))

def fibo(n) :
    if n==0 :
        FIBO[n] = 0
    elif n ==1 :
        FIBO[n] = 1
    else :
        # if we have never computed the value of fib(n)
        # then store it to the array before returning it
        if FIBO[n] == -1:
            FIBO[n] = fibo(n-1) +fibo(n-2)
        # if we already know the value of fib(n)
        # there is no need to calculate it all over again
    return FIBO[n]
    
print(fibo(7))

# Now you can even calculate fibonacci number of even higher numbers
print(fibo(1000))


