import java.util.*;

public class MergeQueues {

    public static List<Character> merge(List<Character> queueOne, List<Character> queueTwo){
        // merge() is a function that takes two queues of sorted items
        // as  arguments and  returns  a  queue  that  results  from
        // merging  the  queues into  sorted  order. 
        List<Character> orderedList = new ArrayList<Character>();

        // add the characters to a list in sorted ordered. Because they are queues
        // we only get the first element and remove the first element. First in First
        // Out.
        while (0 < queueOne.size() && 0 < queueTwo.size()){
            if (queueOne.get(0) < queueTwo.get(0)){
                orderedList.add(queueOne.get(0));
                queueOne.remove(0);
            }
            else if (queueTwo.get(0) < queueOne.get(0)){
                orderedList.add(queueTwo.get(0));
                queueTwo.remove(0);
            }
        
        }

        // if our queues still have items in it then we add them
        // the remaining ones to our ordered list
        if (queueOne.size()>0){
            while(0 < queueOne.size()){
                orderedList.add(queueOne.get(0));
                queueOne.remove(0);
            }
        }

        if (queueTwo.size()>0){
            while(0 < queueTwo.size()){
                orderedList.add(queueTwo.get(0));
                queueTwo.remove(0);
            }
        }

        // Return our ordered list
        return orderedList;
    }    
    public static void main(String []args) {
        List<Character> queueOne = new ArrayList<Character>();
        List<Character> queueTwo = new ArrayList<Character>();

        queueOne.add('A');
        queueOne.add('B');
        queueOne.add('C');
        queueOne.add('D');
        queueOne.add('E');
        queueOne.add('F');
        queueOne.add('G');
        queueOne.add('H');
        queueOne.add('I');
        queueOne.add('J');
        queueOne.add('K');
        queueOne.add('L');
        queueOne.add('M');

        queueTwo.add('N');
        queueTwo.add('O');
        queueTwo.add('P');
        queueTwo.add('Q');
        queueTwo.add('R');
        queueTwo.add('S');
        queueTwo.add('T');
        queueTwo.add('U');
        queueTwo.add('V');
        queueTwo.add('W');
        queueTwo.add('X');
        queueTwo.add('Y');
        queueTwo.add('Z');


        List<Character> merged = merge(queueOne, queueTwo);
        System.out.println(merged);
   }  
}