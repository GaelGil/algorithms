n = [5,4,3,2,1,6,7,8,9,10,0,-1,11,-2,12]


def get_max(n:list) -> int:
    max_num = n[0]
    for i in n:
        if i < max_num:
            pass
        else:
            max_num = i
    return max_num


print(get_max(n))