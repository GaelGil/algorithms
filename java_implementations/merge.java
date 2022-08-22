import java.util.*;

public class merge {

   /* This is my first java program.
    * This will print 'Hello World' as the output
    */

    public static List<Integer> mergeList(List<Integer> numsOne, List<Integer> numsTwo){
        List<Integer> merged = new ArrayList<>();

        int i = 0;
        int j = 0;
        while (i < numsOne.size() && j < numsTwo.size()){
            if (numsOne.get(i) < numsTwo.get(j)){
                merged.add(numsOne.get(i));
                i++;
            }
            else if (numsTwo.get(j) < numsOne.get(i)){
                merged.add(numsTwo.get(j));
                j++;
            }
            else if (numsOne.get(i) == numsTwo.get(i)){
                merged.add(numsOne.get(i));
                merged.add(numsTwo.get(j));
                i++;
                j++;
            }
        }


        if (i < numsOne.size()){
            while(i < numsOne.size()){
                merged.add(numsOne.get(i));
                i++;
            }
        }
        if (j < numsTwo.size()){
            while(j < numsTwo.size()){
                merged.add(numsTwo.get(j));
                j++;
            }  
        }
        return merged;
    }

   public static void main(String []args) {
    List<Integer> numsOne = new ArrayList<>();
    List<Integer> numsTwo = new ArrayList<>();

    numsOne.add(4);
    numsOne.add(8);
    numsOne.add(9);
    numsOne.add(10);
    numsOne.add(34);
    numsOne.add(50);

    numsTwo.add(4);
    numsTwo.add(11);
    numsTwo.add(12);
    numsTwo.add(10);
    numsTwo.add(23);
    numsTwo.add(60);
    numsTwo.add(70);
    numsTwo.add(80);


    List<Integer> mergedList = mergeList(numsOne, numsTwo);
    System.out.println(mergedList);

   }
}