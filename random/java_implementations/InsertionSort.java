import java.util.*;

public class InsertionSort {

    public static List<Integer> sortList(List<Integer> nums){
        for (int i = 1; i < nums.size(); i++){
            int right = nums.get(i);
            while (i > 0 && nums.get(i-1) > right){
                int temp = nums.get(i);
                nums.set(i, nums.get(i-1));
                nums.set(i-1, temp);
                i--;
            }
        }
        return nums;
    }
    public static void main(String []args) {
        List<Integer> nums = new ArrayList<>();
        nums.add(2);
        nums.add(1);
        nums.add(34);
        nums.add(9);
        nums.add(50);
        nums.add(4);
        List<Integer> sortedNums = sortList(nums);
        System.out.println(sortedNums);
   }
}