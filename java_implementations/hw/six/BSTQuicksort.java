
import java.util.*;


public class BSTQuicksort{
    private Node root;

    // default constructor
    BSTQuicksort(){
        this.root = null;
    }

    // second constructor
    BSTQuicksort(int val){
        this.root = new Node(val);       
    }

    // get root node
    public Node getRoot(){
        return this.root;
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

    public void generateTree(List<Integer> arr){

        for (int i = 1; i < arr.size(); i++){
            insert(arr.get(i));
        }

    }

    public void sort(List<Integer> arr, int start, int end) {
		if (start < end) {
			int pIndex = partition(arr, start, end);
			sort(arr, start, pIndex - 1);
			sort(arr, pIndex + 1, end);
		}
	}

	public int partition(List<Integer> arr, int start, int end) {
		int pivot = arr.get(end);
		int partitionIndex = start;
		for (int i = start; i < end; i++) {
			if (arr.get(i) <= pivot) {
				swap(arr, i, partitionIndex);
				partitionIndex++;
			}
		}
		swap(arr, partitionIndex, end);
		return partitionIndex;
	}

	public void swap(List<Integer> arr, int i, int j) {
        int temp = arr.get(i);
        arr.set(i, arr.get(j));
        arr.set(j, temp);

	}

    public static List<Integer> generateArray(int size){
        // generate an array of size `size`
        List<Integer> arr = new ArrayList<Integer>(Collections.nCopies(size, 0));   
        for(int i = 0; i < arr.size(); i++) {
          arr.set(i, (int)(Math.random()*20 + 1));

        }


        return arr;
    }


    public static void main(String []args) {

        // create a binary tree with these 
        // values 5 3, 2, 8, 4, 6, 10
        // BSTQuicksort tree = new BSTQuicksort(5);

        // generate array
        List<Integer> arr = generateArray(10000);

        // use array given to create a bst
        long treeStartTime = System.nanoTime();
        BSTQuicksort tree = new BSTQuicksort(arr.get(0));
        tree.generateTree(arr);
        long treeEndTime   = System.nanoTime();
        long treeTotalTime = treeEndTime - treeStartTime;
        System.out.println(treeTotalTime);

        // perform quicksort on given array
        long sortStartTime = System.nanoTime();
        tree.sort(arr, 0, arr.size()-1);
        long sortEndTime   = System.nanoTime();
        long sortTotalTime = (sortEndTime - sortStartTime)-treeTotalTime;
        System.out.println(sortTotalTime);




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