from typing import Counter


sample_string = 'aabcccccaaa'

def string_compression(sample_string:str) -> str:
    if len(set(list(sample_string))) == len(list(sample_string)):
        return sample_string
    counter = 1
    answer = [] 
    for i in range(len(sample_string)):
        print(sample_string[i])
        if sample_string[i] == sample_string[i+1]:
            counter +=1
            print('here')
        else:
            print('also here')
            answer.append(f'{sample_string[i]}{counter}')
            counter = 1
    print()
    print(answer)
    return ''.join(answer)


print(string_compression(sample_string))


def string_compression(sample_string:str) -> str:
    counter = 0
    answer = []
    for i in range(len(sample_string)):
        if sample_string[i]:
            counter +=1 