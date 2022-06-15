def count_vowels(sample_string:str) -> int:
    sample_string = sample_string.lower()
    res = 0
    vowels = {'a' : 0, 'e': 0, 'i': 0, 'o':0, 'u':0}
    for i in sample_string:
        if i in vowels:
            res += 1

    return res

print(count_vowels('The quick Brown Fox jumps'))


def get_max(nums:list) -> int:
    current_max = nums[0]
    for i in nums:
        if i > current_max:
            current_max = i
    return current_max