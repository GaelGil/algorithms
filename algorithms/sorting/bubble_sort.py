nums = [[3, 10, 5, 12, 9, 20], [2, 8, 5, 3, 9, 4, 1]]


def bubble_sort(nums):
    """Function to perform bubble sort. We do this by iterating through
    the entire list. For each iteration we iterate again checking for
    pairs (j, j+1). If j is greater than j+1 then we swap it.
    The time complexcity of this is O(n^2) because we have to iterate
    through the list once and within that iterate through it again. 

    Parameters
    ----------
    nums: list
        The unsorted list that we want to sort

    Returns
    -------
    list
        The list but its now sorted
    """
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
            continue

    return nums

print(bubble_sort(nums[0]))
print(bubble_sort(nums[1]))

