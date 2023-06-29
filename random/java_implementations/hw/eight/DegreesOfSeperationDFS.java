import java.util.ArrayList;

public class DegreesOfSeperationDFS {
 
    
    public static void main(String args[]){
        Graph graph = new Graph();

        // populate the graph
        graph.addEdge("DFW", "PHX");
        graph.addEdge("ORD", "DFW");
        graph.addEdge("ORD", "PHX");
        graph.addEdge("ATL", "HOU");
        graph.addEdge("DEN", "PHX");
        graph.addEdge("PHX", "LAX");
        graph.addEdge("JFK", "ORD");
        graph.addEdge("DEN", "LAS");
        graph.addEdge("DFW", "HOU");
        graph.addEdge("ORD", "ATL");
        graph.addEdge("LAS", "LAX");
        graph.addEdge("ATL", "MCO");
        graph.addEdge("HOU", "MCO");
        graph.addEdge("LAS", "PHX");

        // get the number of paths
        System.out.println(graph.getPaths("DFW", "PHX"));
        System.out.println(graph.getPaths("ORD", "DFW"));
        System.out.println(graph.getPaths("ORD", "PHX"));
        System.out.println(graph.getPaths("ATL", "HOU"));
        System.out.println(graph.getPaths("DEN", "PHX"));
        System.out.println(graph.getPaths("PHX", "LAX"));
        System.out.println(graph.getPaths("JFK", "ORD"));
        System.out.println(graph.getPaths("DEN", "LAS"));
        System.out.println(graph.getPaths("DFW", "HOU"));
        System.out.println(graph.getPaths("ORD", "ATL"));
        System.out.println(graph.getPaths("LAS", "LAX"));
        System.out.println(graph.getPaths("ATL", "MCO"));
        System.out.println(graph.getPaths("HOU", "MCO"));
        System.out.println(graph.getPaths("LAS", "PHX"));



        // System.out.println(graph.printGraph());

        graph.printGraph();


        

    }
}