# def reverese_recurse(my_str:str)-> str:
#     if my_str == None:
#         return 0
#     current = my_str[0]
#     print(current)
#     # print(' ')
#     reverese_recurse(my_str[1:])
#     print(current, end=' ')   

def other_reverse(my_str:str) -> str:
    return (my_str[::-1])

a_string = 'hello'
# reverese_recurse(a_string)
print(other_reverse(a_string))