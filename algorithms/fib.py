

def fib(fib_one, fib_two):
    next_ = fib_one + fib_two
    print(next_)
    if fib_two > 10:
        return
    fib(fib_two, next_)
    return



fib(0,1)