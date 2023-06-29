import java.util.*;

public class Graph {

    private Map<String, List<String>> adjacencyList;

    // initialize graph
    public Graph() {
        adjacencyList = new HashMap<String, List<String>>();
    }

    // function to add a vertext. This adds a vertex to dictionary as 
    // the key. The value will be a empty linked list 
    public void addVertex(String vertex) {
        adjacencyList.put(vertex, new LinkedList<String>());
    }

    // Add an edge to a given vertex
    public void addEdge(String v, String e) {
        // if the vertex does not currently exist as a vertex add it
        if (!adjacencyList.containsKey(v)) {
            addVertex(v);
        }
        // if the edge does not currenrtly exist as a vertex add it and it
        // it will point back to the vertex we are trying to add
        // This below make sure we create a undirected graph.
        if (!adjacencyList.containsKey(e)) {
            addEdge(e, v);
        }
        // add the edge to the vertex
        adjacencyList.get(v).add(e);
    }

    // display the graph
    public void printGraph() {
        System.out.println(adjacencyList);
    }

    // function to get the number of paths connecting two verticies.

    public String getPaths(String v, String vTwo){
        int paths = 0; // count the paths
        Stack<String> stack = new Stack<String>(); // stack for dfs
        stack.push(v); // add the vertex we start at
        // dictionary to keep track of visited verticies
        Map<String, Integer> visited = new HashMap<String, Integer>();
        // perform dfs
        while (!stack.isEmpty()){
            String current_vertex = stack.pop();
            // if during our traversal from one vertex to another we see 
            // a vertex once and then again that means that there are
            // 1 + 1 paths. Everytime we see the vertex again its +1.
            if (visited.containsKey(current_vertex)){
                paths += 1;
            }
            if (!visited.containsKey(current_vertex) && adjacencyList.containsKey(current_vertex)) {
                visited.put(current_vertex, 0);
                List<String> neighbors = adjacencyList.get(current_vertex);
                for (String neighbor : neighbors) {
                    stack.push(neighbor);
                }
            }
        }


        return "# of paths " + paths + " from: " + v + " to: " + vTwo;
    }






}