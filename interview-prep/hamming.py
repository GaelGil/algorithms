def hammingDistance(x: int, y: int) -> int:
    num_of_changes = 0
    x = list(bin(x)[2:].zfill(8))
    y = list(bin(y)[2:].zfill(8))

    for i in range(len(x)):
        if x[i] != y[i]:
            num_of_changes += 1
    
    return num_of_changes

print(hammingDistance(1 ,4))