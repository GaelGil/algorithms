def to_camel_case(text):
    """
    this function takes in a string as its argument
    and checks if it has blank spaces, if it does
    it replaces it and returns something else
    """
    NO_SPACE = ''
    BLANK_SPACE = ' '
    A_SPACE = '_'
    for i in text:
        if i == A_SPACE:
            new_string = text.replace(A_SPACE, BLANK_SPACE)
    tokens = new_string.split()
    new_list = []
    for x in tokens:
        new_list.append(x.capitalize())
    return NO_SPACE.join(new_list)
 

my_string = "_this_is_my_string_"
another_string = "_things_are _spce__there_things here_"
print(to_camel_case(another_string))
print(to_camel_case(my_string))
