import java.util.*;

public class UseDatastructures {

   public static void main(String []args) {
    // use Tree
    Tree myTree = new Tree(10);
    myTree.insert(6);
    myTree.insert(11);
    myTree.insert(15);
    myTree.insert(2);
    myTree.bfs();
    System.out.println();
    myTree.dfs(myTree.getRoot());


    // use Heap

    // use Graph

    
   }
}