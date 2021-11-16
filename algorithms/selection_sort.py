

sample_list = [100, 2, 23 , 8, 12 , 67]

def selection_sort(nums:list) -> list:
    # loop through all possible pairs
    for i in range(len(nums)-1):
        # index of the current min
        current_min = i
        for j in range(i+1, len(nums)):
            # if we find a new minumin we set `current_min` 
            # to our new found min
            if nums[j] < nums[current_min]:
                current_min = j
        # swap the vales
        temp = nums[i]
        nums[i] = nums[current_min]
        nums[current_min] = temp

    return nums


print(selection_sort(sample_list))