
import java.util.*;


public class BST{
    private Node root;

    // default constructor
    BST(){
        this.root = null;
    }

    // second constructor
    BST(int val){
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

    // insert a node into the tree
    public void insert(int data){
        if (this.root == null){
            this.root = new Node(data);
        }
        else {
            insert(data, this.root);
        }
    }

    // recursivly insert a node
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

    // breadth first search to display tree in level order
    public void bfs(){
        List<Node> queue = new ArrayList<>();
        queue.add(this.root);
        while (queue.size() > 0 ){
            Node currentNode = queue.get(0);
            System.out.println(currentNode.val);
            queue.remove(0);
            if (currentNode.left != null){
                queue.add(currentNode.left);
            }
            if (currentNode.right != null){
                queue.add(currentNode.right);
            }
        }
    }


    public void sumTree(Node currentNode){
        if (currentNode != null){
            sumTree(currentNode.right);
            sumTree(currentNode.left);
            System.out.println(currentNode.val);

            if (currentNode.right != null){
                currentNode.val = currentNode.val+currentNode.right.val;
            }
            if (currentNode.left != null){
                currentNode.val = currentNode.val+currentNode.left.val;
            }
        }
    }


    public static void main(String []args) {

        // create a binary tree with these 
        // values 5 3, 2, 8, 4, 6, 10
        BST treeA = new BST(5);
        treeA.insert(3);
        treeA.insert(2);
        treeA.insert(8);
        treeA.insert(4);
        treeA.insert(6);
        treeA.insert(10);

        // display the tree
        treeA.bfs();

        // try and sum the tree
        treeA.sumTree(treeA.getRoot());
        System.out.println();
        // display the new tree
        treeA.bfs();


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