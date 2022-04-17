nums = [1, 3, 4, 6, 9, 11, 33, 99, 1089, 3454, 199089] # ordered numbers

def recursive(nums, left, right, target):
    """Function to perform bubble sort. We do this by iterating through
    the entire list. For each iteration (i) we iterate again checking for
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
    return

def iterative(nums, target):
    """Function to perform bubble sort. We do this by iterating through
    the entire list. For each iteration (i) we iterate again checking for
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
    left = 0
    right = len(nums)-1
    while left <= right:
        if nums[left] == target:
            return f'found at index {left}'
        elif nums[right] == target:
            return f'found at index {right}'
        if nums[left] < target:
            left += 1
        elif nums[right] > target:
            right -= 1

    return 'not in list'


print('Iterative')
print(iterative(nums, 11))
print(iterative(nums, 10))
print()
print('Recursive')
print(recursive(nums, 33))
print()
print(recursive(nums, 10))