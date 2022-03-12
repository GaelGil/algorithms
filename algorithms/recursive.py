

def even(num:int):
    print(num)
    if num % 2 != 0:
        return f'invalid number'
    if num == 2:
        return num
    else:
        return even(num-2)


# even(50)



def fib(num:int):
    if num <=1:
        return num
    else:
        return fib(num-1)+fib(num-2)


print(fib(3))


