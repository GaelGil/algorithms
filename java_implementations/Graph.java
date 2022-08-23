import java.util.*;

public class Graph {
   private Dictionary graph = new Hashtable();
 

   Graph(char node){
      this.graph.put(node, 0);
   }

   Graph(char node, Dictionary neighbors){
      this.graph.put(node, neighbors);
   }

   public void insert(char node, Dictionary neighbors){
      if (node in graph){
         System.out.println("already in graph");
      }
      else{
         this.graph.put(node, neighbors);
      }
   }

   public void bfs(){
      // List<Node> queue = new ArrayList<>();
      // queue.add(this.root);
      // while (queue.size() > 0 ){
      //    Node currentNode = queue.get(0);
      //    queue.remove(0);
      //    System.out.println(currentNode.val);
      //    if (currentNode.left != null){
      //       queue.add(currentNode.left);
      //    }
      //    if (currentNode.right != null){
      //       queue.add(currentNode.right);
      //    }
      // }
   }

}

