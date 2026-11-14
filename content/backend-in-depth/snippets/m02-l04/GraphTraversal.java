import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

public class GraphTraversal {
    static List<List<Integer>> graph(int vertices, int[][] edges) {
        List<List<Integer>> adjacency = new ArrayList<>();
        for (int v = 0; v < vertices; v++) {
            adjacency.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adjacency.get(edge[0]).add(edge[1]);
            adjacency.get(edge[1]).add(edge[0]);
        }
        return adjacency;
    }

    static List<Integer> bfs(List<List<Integer>> adjacency, int start) {
        List<Integer> order = new ArrayList<>();
        boolean[] seen = new boolean[adjacency.size()];
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        seen[start] = true;
        while (!queue.isEmpty()) {
            int v = queue.remove();
            order.add(v);
            for (int w : adjacency.get(v)) {
                if (!seen[w]) {
                    seen[w] = true;
                    queue.add(w);
                }
            }
        }
        return order;
    }

    static void dfs(List<List<Integer>> adjacency, int v, boolean[] seen, List<Integer> order) {
        seen[v] = true;
        order.add(v);
        for (int w : adjacency.get(v)) {
            if (!seen[w]) {
                dfs(adjacency, w, seen, order);
            }
        }
    }

    public static void main(String[] args) {
        List<List<Integer>> adjacency = graph(7, new int[][] {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {3, 4}, {5, 6}});
        System.out.println("bfs " + bfs(adjacency, 0));

        List<Integer> order = new ArrayList<>();
        dfs(adjacency, 0, new boolean[adjacency.size()], order);
        System.out.println("dfs " + order);

        boolean[] seen = new boolean[adjacency.size()];
        int components = 0;
        for (int v = 0; v < adjacency.size(); v++) {
            if (!seen[v]) {
                dfs(adjacency, v, seen, new ArrayList<>());
                components++;
            }
        }
        System.out.println("components " + components);
    }
}
