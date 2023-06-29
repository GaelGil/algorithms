import java.util.*;

public class InderectSort {

    public static List<Character> sort(List<Character> orderedList){
        // sort() in IndirectSort.java that indirectly sorts a[]
        // using insertion sort, ie, not by rearranging a[], but
        // by returning an array perm[]  such that perm[i] is the
        // index of the ith smallest entry in a[]. 

        for (int i = 1; i < orderedList.size(); i++){
            char right = orderedList.get(i);
            while(i > 0 && orderedList.get(i-1) > right){
                char temp = orderedList.get(i);
                orderedList.set(i, orderedList.get(i-1));
                orderedList.set(i-1, temp);
                i--;
            }
        }


        return orderedList;
    }
    public static void main(String []args) {
        List<Character> arr = new ArrayList<Character>();
        arr.add('I');
        arr.add('N');
        arr.add('D');
        arr.add('I');
        arr.add('R');
        arr.add('E');
        arr.add('C');
        arr.add('T');
        arr.add('I');
        arr.add('N');
        arr.add('S');
        arr.add('E');
        arr.add('R');
        arr.add('T');
        arr.add('I');
        arr.add('O');
        arr.add('N');
        arr.add('S');
        arr.add('O');
        arr.add('R');
        arr.add('T');
        arr.add('E');
        arr.add('X');
        arr.add('A');
        arr.add('M');
        arr.add('P');
        arr.add('L');
        arr.add('E'); 

        List<Character> sorted = sort(arr);
        System.out.println(sorted);

   }
}