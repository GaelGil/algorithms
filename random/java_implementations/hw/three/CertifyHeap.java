public class CertifyHeap {
    // Return true of v is less than w and false otherwise.
    private static boolean less(Comparable v, Comparable w) {
       return (v.compareTo(w) < 0);
   }

   // Return true if a[] represents a maximum-ordered heap and false
   // otherwise. Remember to index from 1.
   private static boolean maxOrderedHeap(Comparable[] a) {
       //INSERT DODE HERE
       // Iterate throguh the array heap. The parent node will be i and the children will be 2*i and 2*i+1
       // If at any point the parent node is not greater than its children we will return false. Additionally
       // because we are only iterating the array once it will be linear time. Also we start i=1 because the
       // head we leave as empty. The root node will be at i=1. To do this assignment I went to the computer 
       // science tutoring room on the second floor. 
       for (int i = 1; i <= (a.length-2)/2; i++){
           int parent = a[i];
           int leftChild = a[2*i];
           int rightChild = a[(2*i)+1];
           if (less(parent, leftChild)){
               return (false);
           }
           if (less(parent, rightChild)){
               return (false);
           }
       }
       // at this point we are done and had no issue so we return
       return (true);
   }

   // Test client. [DO NOT EDIT]
   public static void main(String[] args) {
       String[] a = StdIn.readAllStrings();
       // StdOut.println(maxOrderedHeap(a));
       System.out.println(maxOrderedHeap(a));
   }
}
