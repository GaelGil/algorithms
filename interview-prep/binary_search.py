
sample = [1, 3, 4, 6, 9, 11, 33, 99, 1089, 3454, 199089] # ordered numbers


def binary_search(sample_list:list, target:int):
    middle = int(len(sample_list)/2)
    left = sample_list[:middle]
    right= sample_list[middle:]
    if sample_list[middle] == target:
        return 'found'
    if sample_list[middle] > target:
        binary_search(left, target)
    if sample_list[middle] < target:
        binary_search(right, target)
    return f'found: {target}'

print(binary_search(sample, 3))