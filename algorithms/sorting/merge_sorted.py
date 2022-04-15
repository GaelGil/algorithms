nums_one = [1, 3, 4, 5, 7]
nums_two = [2, 5, 6]


def merge(nums_one:list, nums_two:list) -> list:
    """Function to merge two sorted lists. We do this by iterating through
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
    i = 0
    j = 0
    answer = []
    while i < len(nums_one) and j < len(nums_two):
        if nums_one[i] < nums_two[j]:
            answer.append(nums_one[i])
            i += 1
        elif nums_two[j] < nums_one[i]:
            answer.append(nums_two[j])
            j += 1
        elif nums_one[i] == nums_two[j]:
            answer.append(nums_one[i])
            answer.append(nums_two[j])
            i += 1
            j += 1

    # print(len(nums_two))
    if i < len(nums_one):
        answer += nums_one[i:]
    if j < len(nums_two):
        answer += nums_two[j:]
    return answer

print(merge(nums_one=nums_one, nums_two=nums_two))