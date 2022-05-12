nums = [[3, 10, 5, 12, 9, 20], [2, 8, 5, 3, 9, 4, 1]]


def selection(nums):
    """Function to perform insertion sort.

    Parameters
    ----------
    nums: list
        The unsorted list that we want to sort

    Returns
    -------
    list
        The list but its now sorted
    """
    for i in range(1, len(nums)):
        right = nums[i]
        while nums[i-1] > right:
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
            i -=1

    return nums

print(selection(nums[0]))
print(selection(nums[1]))
