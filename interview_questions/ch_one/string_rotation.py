
s1 = 'waterbottle'
s2 = 'elttobretaw'

def is_substring(s1:str, s2:str) -> bool:
    if len(s1) > len(s2) or len(s1) < len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[-(i+1)]:
            return False
    return True

print(is_substring(s1, s2))
