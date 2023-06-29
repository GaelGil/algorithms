/*
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
You may assume that each input would have exactly one solution and you may not use the same element twice.

// Approach it using Binary Search. We can also use two pointers


      target = 9

          [2,7,11,15]
           ^.^  


*/

import java.util.*;
class unsortedTwoSum {


  
  public static void main(String[] args) {
    int[] result = nums(new int[]{2,7,11,15}, 9);
    for(int i: result){
        System.out.print(i + " ");
    }
  }

/**
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].



    Ex 2: Input: nums = [3,2,4], target = 6
          Output: [1,2]   
        {value: index}
        target - value = difference // 6 - 3 = 3 
 */


  public static int[] nums(int[] nums, int target){
    // map of values, array indexes
    Map<Integer, Integer> map = new HashMap<>();
    for(int i = 0; i < nums.length; i++){
        int compliment = target - nums[i];
        if(map.containsKey(compliment)){
            return new int[]{i, map.get(compliment)};
        }
        map.put(nums[i], i);
    }
    return new int[]{};
 }
  
}