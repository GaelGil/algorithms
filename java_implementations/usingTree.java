// package Tree;
// import Tree.Tree;
import java.util.*;

public class usingTree {

   public static void main(String []args) {
    Tree myTree = new Tree(10);
   // System.out.println(myTree.getRootVal());
   myTree.insert(6);
   myTree.insert(11);
   myTree.insert(15);
   myTree.insert(2);
   // System.out.println(myTree.getRoot().right.val);
   myTree.bfs();
   myTree.dfs();
   }
}