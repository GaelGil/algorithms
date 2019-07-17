#1.1
MY_STRING = 'string is not unique'

# def all_unique(a_string):
#     if len(a_string) > 128:
#         return False
#     char_set = []
#     for i in a_string:
#         char_set.append(i)    
#         val = a_string[i]
#         if char_set[val]:
#             return False
#     return True    

#     if len(a_string) > 128:
#         return False
#     char_set = []
#     bool(char_set)
#     for i in range(len(a_string)):
#         val = a_string[i]
#         int(val)
#         if char_set[val]:
#             return False
#     return True


# all_unique(MY_STRING)
def isUniqueString(a_string):
    checker = 0
    for i in range(len(a_string)):
        val = i
        if checker and i < val > 0:
            print()
    print('yes')
isUniqueString(MY_STRING)

#1.2


#1.3
TWENTY_PERCENT = '%20'
the_string = 'the kid ate icecream'
def replaceSpaces(a_string):
    """
    this function takes in a string as its argument
    and checks if it has blank spaces, if it does
    it replaces it and returns something else
    """
    for i in a_string:
        if i == ' ':
            new_string = a_string.replace(' ', TWENTY_PERCENT)
    return new_string

print(the_string)
print(replaceSpaces(the_string))


# def to_camel_case(text):
#     """
#     this function takes in a string as its argument
#     and checks if it has blank spaces, if it does
#     it replaces it and returns something else
#     """
#     NO_SPACE = ''
#     for i in text:
#         if i == '_':
#             new_string = text.replace('_', " ")
#     tokens = new_string.split()
#     # index = tokens
#     # print(index)
#     new_list = []
#     for x in tokens:
#         new_list.append(x.capitalize())
#     print(NO_SPACE.join(new_list))
#     # print(new_string)
 

# my_string = "_this_is_my_string"
# to_camel_case(my_string)

