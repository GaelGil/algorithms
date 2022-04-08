def exp(num:int, power:int):
    if power>=1:
        return num * exp(num, power-1)
    else:
        return 1

print(exp(4,4))
