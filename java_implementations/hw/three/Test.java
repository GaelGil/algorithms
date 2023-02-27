import java.util.*;

public class Test {
    public static void main(String []args) {
        List<Integer> nums = new ArrayList<>();
        nums.add(0);
        nums.add(2);
        nums.add(1);
        nums.add(34);
        nums.add(9);
        nums.add(50);
        nums.add(3);
        nums.add(4);
        nums.add(4);
        nums.add(10);

        System.out.println(nums.size()/2);
        for (int i = 1; i <= (nums.size()-2)/2; i++){
            int parent = nums.get(i);
            int leftChild = nums.get(2*i);
            int rightChild = nums.get((2*i)+1);
            System.out.println(parent);
            System.out.println(leftChild);
            System.out.println(rightChild);
            if (parent < leftChild){
                System.out.println("false");
            }
            if (parent < rightChild){
                System.out.println("false");
            }
        }

    
        
       }
    
}




