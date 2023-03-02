import java.util.*;

public class ModefiedCountingSort {

   public static void main(String []args) {

    // List<Integer> k = new ArrayList<>();
    int k = 50; // set to 50 but can be anything
    List<Integer> A = new ArrayList<>();
    List<Integer> C = new ArrayList<>();

    for (int i = 1; i <= k; i++) {
        C.add(0);
    }

    for (int j = 1; j <= A.size(); j++) {
        C.add(A.get(j), A.get(j)+1);
    }

    for (int i = 2; i <= k; i++) {
        C.add(C.get(i), (C.get(i)+C.get(i-1)));
    }

    for (int j = A.size(); j >= 1; j--){
        A.add(C.get(A.get(j)), A.get(j));
        C.add(A.get(j), (C.get(A.get(j))-1));
    }

   }

}