nums = [[3, 10, 5, 12, 9, 20], [2, 8, 5, 3, 9, 4, 1]]


def selection(nums):
    """Function to perform selection sort.

    Parameters
    ----------
    nums: list
        The unsorted list that we want to sort

    Returns
    -------
    list
        The list but its now sorted
    """
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1, len(nums)):
            print(f'nums[i]: {nums[i]}')
            print(f'nums[j]: {nums[j]}')
            print()
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            temp = nums[i]
            nums[i] = nums[min_index]
            nums[min_index] = temp


    return nums

print(selection(nums[0]))
print(selection(nums[1]))
