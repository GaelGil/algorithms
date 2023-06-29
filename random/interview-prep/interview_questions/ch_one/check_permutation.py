

s1 = 'abc'
s2 = 'acb'

s3 = 'bca'
s4 = 'cba'

s5 = 'cab'
s6 = 'bac'

s7 = 'wasd'
s8 = 'sawf'

s9 = 'wasd'
s10 = 'saw'

def check_permutation(s1:str, s2:str):
    """
    check if two strings are a permutation. A permutation is a rearangement of letters.
    For this we check if either string has more characters than one if so they cant be
    a permutation. If we pass that then we can 
    """
    print()
    if len(s1) > len(s2) or len(s1) < len(s2):
        return False
    s1_dict = {}
    for i in s1:
        s1_dict[i] = i
    for i in range(len(s2)):
        if s2[i] not in s1_dict:
            return False

    return True


print(check_permutation(s1, s2))

print(check_permutation(s3, s4))

print(check_permutation(s5, s6))

print(check_permutation(s7, s8))

print(check_permutation(s9, s10))



def check_permutation_zip(s1:str, s2:str):
    """
    Check if two strings are a permutation. For this we do the same intial check we do
    in the first function but we add the 
    """
    if len(s1) > len(s2) or len(s1) < len(s2):
        return False
    for (i, j) in zip(sorted(s1), sorted(s2)):
        if i != j:
            return False
    return True




print()
print(check_permutation_zip(s1, s2))
print(check_permutation_zip(s3, s4))
print(check_permutation_zip(s5, s6))
print(check_permutation_zip(s7, s8))
print(check_permutation_zip(s9, s10))

