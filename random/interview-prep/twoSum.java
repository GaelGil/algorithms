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


class twoSum {

  private static int[] result = new int[2];
  
  public static void main(String[] args) {
   int[] result = nums(new int[]{2,7,11,15}, 9);
  //  Arrays.stream(result).forEach(num -> System.out.print(num + " "));
  for(int i: result){
    System.out.print(i + " ");
  }
    result = numsRecursive(new int[]{2,7,11,15},9);
    for(int i: result){
      System.out.print(i + " ");
    }
  }
  public static int[] nums(int[] array, int target){
    // Set our pointers in order to preform binary search 
    
    int low = 0, high = array.length-1;
    while(low<high){
      int currentSum = array[low] + array[high];
      if(currentSum == target){
        return new int[]{low+1, high+1};
      }
      else if(currentSum < target){
        low++;
      }
      else{
        high--;
      }
    }
    
    return null;
  }
  
  public static int[] numsRecursive(int[] array, int target){
    helperFunction(array,target, 0, array.length-1, 0);
    return result;
  
  }

  private static void helperFunction(int[] array, int target, int low, int high, int currentSum){
    if(currentSum == target){
      result[0] = array[low+1];
      result[1] = array[high+1];
    }
    if(currentSum < target){
      low++;
      helperFunction(array, target, low, high, currentSum + array[low]);
    }
    else{
      high--;
      helperFunction(array, target, low, high, currentSum + array[high]);
    }

  }


}