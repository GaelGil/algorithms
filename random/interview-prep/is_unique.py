# to check if string has all characters in
# python we can do this
def using_sets(a_string):
    new_string = set(list(a_string))
    if len(a_string) == len(new_string):
        return('is unique')
    else:
        return('not unique')


a_string = "where"
other_string = 'other'
print(using_sets(other_string))
print(using_sets(a_string))


# using a dictionary/hashmap
def using_dict(a_string):
    a_string = list(a_string)
    char_dict = {}
    for i in range(len(a_string)):
        if a_string[i] in char_dict:
            return ('not unique')
        char_dict[a_string[i]] = i
    return ('unique')

print(using_dict(a_string))
print(using_dict(other_string))


def one_way(a_string, b_string):
    a_list = (a_string)
    b_list = (b_string)
    steps = 0
    if len(a_list) - len(b_list) <=1:
        return True
    for i in range(len(b_string)):
        if a_list[i] == b_list[i]:
            pass
        else:
            steps +=1
    if steps > 1:
        return False
    elif steps <= 1:
        return True
        
print(one_way("pale", "ple"))
print(one_way("pales", "ple"))
print(one_way("pale", "bale"))
print(one_way("pale", "bake"))
