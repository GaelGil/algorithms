def count_down(num):
    if num>=1:
        print(num)
        count_down(num-1)
    return    

def count_to(iterration, num):
    if iterration != num:
        print(iterration)
        iterration += 1
        count_to(iterration, num)
    else:
        print(iterration)
        return iterration
    return


print('Count Down')
count_down(10)
print()
print('Count Up')
count_to(1, 10)