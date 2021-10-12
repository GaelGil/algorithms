sample_string = 'aabcccccaaa'

def string_compression(sample_string:str) -> str:
    if len(set(list(sample_string))) == len(list(sample_string)):
        return sample_string
    new_string = []
    counter = 0
    for i in range(len(new_string)-1):
        if new_string[i] == new_string[i+1]:
            counter 
    return new_string


print(string_compression(sample_string))