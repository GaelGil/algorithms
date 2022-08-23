import java.util.*;


public class Tree{
    private Node root;

    Tree(){
        this.root = null;
    }

    Tree(int val){
        this.root = new Node(val);       
    }

    // get root node
    public Node getRoot(){
        return this.root;
    }

    // get root node value
    public int getRootVal(){
        return this.root.val;
    }

    public void insert(int data){
        if (this.root == null){
            this.root = new Node(data);
        }
        else {
            _insert(data, this.root);
        }
    }

    public void _insert(int data, Node currentNode){
        if (data < currentNode.val){
            if (currentNode.left == null){
                currentNode.left = new Node(data);
            }
            else {
                _insert(data, currentNode.left);
            }
        }
        else if (data >= currentNode.val){
            if (currentNode.right == null){
                currentNode.right = new Node(data);
            }
            else {
                _insert(data, currentNode.right);
            }
        }
    }

    public void dfs(){
        List<Node> stack = new ArrayList<>();
        stack.add(this.root);
    }

    public void bfs(){
        List<Node> queue = new ArrayList<>();
        queue.add(this.root);
        while (queue != null){
            currentNode = queue.popLeft();
            System.out.println(currentNode);
            if (currentNode.left){
                queue.add(currentNode.left);
            }
            if (currentNode.right){
                queue.add(currentNode.right);
            }
        }


    }



//    public static void main(String []args) {
//         insert(10);
//         // System.out.println(this.root);
//         // Node root = new Node(4);
//         // System.out.println(root.val);
//         // root.left = new Node(5);
//         // root.right = new Node(6);
//         // // root(new Node(4), new Node(6));
//         // System.out.println(root.left.val);
//         // System.out.println(root.right.val);
        
//    }
}



class Node{
    int val;
    Node left;
    Node right;
    Node(int val){
        this.val = val;
        this.left = null;
        this.right = null;
        }

}