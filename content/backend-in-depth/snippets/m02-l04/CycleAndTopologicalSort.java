import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CycleAndTopologicalSort {
    enum Status { NEW, ACTIVE, FINISHED }

    static boolean hasCycle(List<List<Integer>> adjacency) {
        Status[] status = new Status[adjacency.size()];
        java.util.Arrays.fill(status, Status.NEW);
        for (int v = 0; v < adjacency.size(); v++) {
            if (status[v] == Status.NEW && visitFindsCycle(adjacency, v, status, new ArrayList<>())) {
                return true;
            }
        }
        return false;
    }

    static boolean visitFindsCycle(List<List<Integer>> adjacency, int v, Status[] status, List<Integer> postorder) {
        status[v] = Status.ACTIVE;
        for (int w : adjacency.get(v)) {
            if (status[w] == Status.ACTIVE) {
                return true;
            }
            if (status[w] == Status.NEW && visitFindsCycle(adjacency, w, status, postorder)) {
                return true;
            }
        }
        status[v] = Status.FINISHED;
        postorder.add(v);
        return false;
    }

    static List<Integer> topologicalOrder(List<List<Integer>> adjacency) {
        Status[] status = new Status[adjacency.size()];
        java.util.Arrays.fill(status, Status.NEW);
        List<Integer> postorder = new ArrayList<>();
        for (int v = 0; v < adjacency.size(); v++) {
            if (status[v] == Status.NEW) {
                visitFindsCycle(adjacency, v, status, postorder);
            }
        }
        Collections.reverse(postorder);
        return postorder;
    }

    static List<List<Integer>> directed(int vertices, int[][] edges) {
        List<List<Integer>> adjacency = new ArrayList<>();
        for (int v = 0; v < vertices; v++) {
            adjacency.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adjacency.get(edge[0]).add(edge[1]);
        }
        return adjacency;
    }

    public static void main(String[] args) {
        int[][] dag = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {3, 4}};
        System.out.println("topological " + topologicalOrder(directed(5, dag)));
        System.out.println("dag has cycle " + hasCycle(directed(5, dag)));

        int[][] withBackEdge = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {3, 4}, {4, 1}};
        System.out.println("with edge 4->1 has cycle " + hasCycle(directed(5, withBackEdge)));
    }
}
