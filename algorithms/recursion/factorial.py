def fact(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * fact(n-1)
    
print(f'4: factorial {fact(4)}')

print(f'0: factorial {fact(0)}')