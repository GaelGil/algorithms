from .merge_sorted import merge


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    left = nums[:int(len(nums)/2)]
    right = nums[int(len(nums)/2):]

    left = merge_sort(left)
    right = merge_sort(right)
    arr = merge(left, right)

    return arr





nums = [241, 4235, 12, 23, 7, 1 ,8, 32]
sorted_ = merge_sort(nums)
print(nums)
print(sorted_)