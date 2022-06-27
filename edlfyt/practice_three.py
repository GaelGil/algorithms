def compare_linear(nums_one:list, nums_two:list) -> int:
    """
    Function to find how many rotations have happened on a list.
    """
    prev = nums_two[0]
    for i in range(len(nums_two)):
        if nums_two[i] < prev:
            return i
    return 0
    



def compare_binary_search(nums_one:list, nums_two:list) -> int:
    left = 0
    right = len(nums_two)-1
    # print(left)
    # print(right)
    while left <= right and left != right:
        mid = int((left+right)/2)
        if nums_two[mid] < nums_two[left]:
            right = mid - 1
        elif nums_two[mid] > nums_two[right]:
            left = mid + 1
    return left




l1= [2,5,6,8,9,10]
l2 = [8,9,10,2,5,6]
# l2 = [10, 2, 5 ,6 ,8, 9]
print(compare_linear(l1, l2))

print(compare_binary_search(l1, l2))