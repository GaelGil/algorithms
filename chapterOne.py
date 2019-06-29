MY_STRING = 'string'


def all_unique(a_string):
    if len(a_string) > 128:
        return False
    char_set = []
    for i in a_string:
        char_set.append(i)    
        val = a_string[i]
        if char_set[val]:
            return False
    return True    

    # if len(a_string) > 128:
    #     return False
    # char_set = []
    # bool(char_set)
    # for i in range(len(a_string)):
    #     val = a_string[i]
    #     int(val)
    #     if char_set[val]:
    #         return False
    # return True


all_unique(MY_STRING)

