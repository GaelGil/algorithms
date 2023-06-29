sample_string = 'this is a sample string'
unique_string = 'abcdefhijklmnopqrstuvwxyz'
MAX_LEN = 27

def is_unique(a_string:str):
    """function to check for unique character string"""
    if len(a_string) > MAX_LEN:
        return False
    if len(set(list(a_string))) < len(list(a_string)):
        return False
    return True


print(is_unique(sample_string))
print(is_unique(unique_string))


def is_unique_dictionary(sample_string:str) -> bool:
    """function to check if a string is unique with dictionary"""
    character_dict = {}
    for i in sample_string:
        if i in character_dict:
            return False
        else:
            character_dict[i] = i
    return True

print()
print(is_unique_dictionary(sample_string))
print(is_unique_dictionary(unique_string))
