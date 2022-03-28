

def iterate_list(nums):
    if nums:
        print(nums.pop())
        iterate_list(nums)
    return

nums = [1, 2, 3, 4, 5]

iterate_list(nums)