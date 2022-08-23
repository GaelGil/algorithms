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
            insert(data, this.root);
        }
    }

    public void insert(int data, Node currentNode){
        if (data < currentNode.val){
            if (currentNode.left == null){
                currentNode.left = new Node(data);
            }
            else {
                insert(data, currentNode.left);
            }
        }
        else if (data >= currentNode.val){
            if (currentNode.right == null){
                currentNode.right = new Node(data);
            }
            else {
                insert(data, currentNode.right);
            }
        }
    }

    public void dfs(){
        List<Node> stack = new ArrayList<>();
        stack.add(this.root);
        while (stack.size() > 0 ){
            Node currentNode = stack.get(stack.size()-1);
            stack.remove(stack.size()-1);
            System.out.println(currentNode.val);
            if (currentNode.left != null){
                stack.add(currentNode.left);
            }
            if (currentNode.right != null){
                stack.add(currentNode.right);
            }
        }

    }

    public void bfs(){
        List<Node> queue = new ArrayList<>();
        queue.add(this.root);
        while (queue.size() > 0 ){
            Node currentNode = queue.get(0);
            queue.remove(0);
            System.out.println(currentNode.val);
            if (currentNode.left != null){
                queue.add(currentNode.left);
            }
            if (currentNode.right != null){
                queue.add(currentNode.right);
            }
        }
    }
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