nums_one = [1, 3, 4, 5, 7]
nums_two = [2, 5, 6]

arr_one = [6, 7, 8, 8, 9]
arr_two = [1, 3, 6, 7, 10]

def merge(nums_one:list, nums_two:list) -> list:
    """Function to merge two sorted lists. 

    Parameters
    ----------
    nums_one: list
        A sorted list
    nums_two: list
        Another sorted list

    Returns
    -------
    list
        The two sorted lists now merged as one.
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

    if i < len(nums_one):
        answer += nums_one[i:]
    if j < len(nums_two):
        answer += nums_two[j:]
    return answer

# print(merge(nums_one=nums_one, nums_two=nums_two))
# print(merge(nums_one=arr_one, nums_two=arr_two))
