s1 = 'pale'
s2 = 'ple'

s3 = 'pales'
s4 = 'pale'

s5 = 'pale'
s6 = 'bale'

s7 = 'pale'
s8 = 'bake'

def one_way(s1:str, s2:str) -> bool:
    """function to check if strings are 1 or 0 edits away to match"""
    changes = 0
    s1_dict = {}
    for i in s1:
        s1_dict[i] = i
    
    for i in range(len(s2)):
        if s2[i] not in s1_dict:
            changes +=1
    return changes == 0 or changes == 1


print(one_way(s1, s2))

print(one_way(s3, s4))

print(one_way(s5, s6))

print(one_way(s7, s8))    