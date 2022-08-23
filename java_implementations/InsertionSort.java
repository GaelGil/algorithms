import java.util.*;

public class insertSort {

    public List<Integer> mergeList(List<Integer> nums){
        for (int i = 1; i < nums.size(); i++){
            int right = nums.get(i);
            int prev = nums.get(i-1);
            while (prev > right && i > 0){
                int temp = nums.get(i);
                nums.get(i) = right;
                right = temp;
                i--;
            }
        }
    }
}