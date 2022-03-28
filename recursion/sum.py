def sum_num(n):
    if n == 0:
        return 0
    return int(n%10) + sum_num(int(n/10))


print(sum_num(345))

def sum_list(nums):
    if nums:
        if len(nums) <= 1:
            return nums[0]
        else:
            n = nums.pop(0)
            return n + sum_list(nums)
    else:
        return 0


print(sum_list([3, 4, 5]))

# n = [2, 1, 4]

# print(n)
# n.pop(0)
# print(n)
 