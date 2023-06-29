import java.util.*;


public class question_1_b {
    
    public static int lumberCuttingproblem(int n, List<Integer> cuts){

        return n;
    }

    public static void main(String[] args) {
        List<Integer> cuts = new ArrayList<>();
        cuts.add(0);
        cuts.add(6);
        cuts.add(18);
        cuts.add(25);
        cuts.add(32);
        cuts.add(42);
        System.out.println(lumberCuttingproblem(42, cuts));
    }
}
