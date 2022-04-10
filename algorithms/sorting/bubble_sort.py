nums = [[3, 10, 5, 12, 9, 20], [2, 8, 5, 3, 9, 4, 1]]


def bubble_sort(nums):
    """
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

