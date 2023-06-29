import edu.princeton.cs.algs4.DirectedEdge;
import edu.princeton.cs.algs4.EdgeWeightedDigraph; 
import edu.princeton.cs.algs4.IndexMinPQ;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Stack;


public class MonotonicShortestPath {
    private double[] distanceTo;    // distTo[v] = distance  of shortest s->v path
    private DirectedEdge[] edgeTo;    // edgeTo[v] = last edge on shortest s->v path
    private IndexMinPQ<Double> priorityQueue;
    
    /**
     * Computes a shortest-paths tree from the source vertex {@code s} to every other
     * vertex in the edge-weighted digraph {@code G}.
     *
     * @param  graph the edge-weighted digraph
     * @param  start the source vertex
     * @param  increasing if true then order is in creasing
     * @return 
     */
    public int getShortestPaths(EdgeWeightedDigraph graph, int start){

        distanceTo = new double[graph.V()];
        edgeTo = new DirectedEdge[graph.V()];

        // set all verticeies to length of infinity
        for (int v = 0; v < graph.V(); v++)
            distanceTo[v] = Double.POSITIVE_INFINITY;
        // set starting vertex distance of 0
        distanceTo[start] = 0.0;

        // relax vertices in order of distance from s
        priorityQueue = new IndexMinPQ<Double>(graph.V());
        priorityQueue.insert(start, distanceTo[start]);
        while (!priorityQueue.isEmpty()) {
            int v = priorityQueue.delMin();
            for (DirectedEdge edge : graph.adj(v))
                relax(edge);
        }
        return 0;
    }

    // edited version of code from https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/DijkstraSP.java.html
    // I edited the code to get the increasing monotonic path. This code works to get the
    // monotically increasing path. However if for example we have a edge from a to b for 5.
    // From b to c its 6 then from c to d its 4 or from c to e its 3. In this case it only 
    // has the option of getting a smaller edge. 
    public void relax(DirectedEdge edge) {
        int current = edge.from(), nextVertex = edge.to();
        // if the distance to the next vertex is greater than the previous vertex
        // then add that instead
            if (distanceTo[nextVertex] > distanceTo[current]) {
                distanceTo[nextVertex] = distanceTo[current];
                edgeTo[nextVertex] = edge;
                if (priorityQueue.contains(nextVertex)){ 
                    priorityQueue.decreaseKey(nextVertex, distanceTo[nextVertex]);
                }
                else {
                    priorityQueue.insert(nextVertex, distanceTo[nextVertex]);
                }
            }
    }

    // more code from https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/DijkstraSP.java.html
    public Iterable<DirectedEdge> pathTo(int v) {
        Stack<DirectedEdge> path = new Stack<DirectedEdge>();
        for (DirectedEdge e = edgeTo[v]; e != null; e = edgeTo[e.from()]) {
            path.push(e);
        }
        return path;
    }



    // A lot of this code is from https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/DijkstraSP.java.html
    // I simply edited the code to make it so that we get the monotincally increasing path. Additionlly
    // I usde tinyEWD.txt for a sample graph.
     public static void main(String[] args) {
        In in = new In(args[0]);
        EdgeWeightedDigraph sampleGraph = new EdgeWeightedDigraph(in);
        MonotonicShortestPath paths = new MonotonicShortestPath();
        int sourceVertex = 1;
        paths.getShortestPaths(sampleGraph, sourceVertex);

        
        // print shortest path 
        for (int t = 0; t < sampleGraph.V(); t++) {
                System.out.printf("%d to %d (%.2f)  ", sourceVertex, t, paths.distanceTo[t]);
                for (DirectedEdge e : paths.pathTo(t)) {
                    System.out.print(e + "   ");
                }
                System.out.println();
        }



    }
}
