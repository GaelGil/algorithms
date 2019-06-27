MY_STRING = 'string'


# def all_unique(a_string):
#     if a_string > 128:
#         print('No')
#     bool(char_set = [])
#     for i in range(len(a_string)):
#         int(val = a_string[i])
#         if char_set[val]:
#             print('No')

#         char_set[val] = True
    
#     return True



def all_unique(a_string):
    checker = 0
    for i in range(len(a_string)):
        val = a_string[i]
        if checker and 1 < val > 0:
            return False
        


all_unique(MY_STRING)
