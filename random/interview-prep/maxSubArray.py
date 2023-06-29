"""
 Maximum Subarray: Given an integer array nums, find the contiguous subarray(next to each other) (containing at least one number) 
 which has the largest sum and return its sum.

 Example 1: Input: nums = [-2,1,-3,4,-1,2,1,-5,4], Output: 6
                                      ^
                        currentWindowSum = 0
                        maxSum = 4
 Explanation: [4,-1,2,1] has the largest sum = 6.

"""

def maxSubArray(nums):
    currentWindowSum = nums[0]
    maxSum = currentWindowSum

    for index in range(1, len(nums)):
        currentWindowSum = max(nums[index], currentWindowSum + nums[index])
        maxSum = max(maxSum, currentWindowSum)
    return maxSum




nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))