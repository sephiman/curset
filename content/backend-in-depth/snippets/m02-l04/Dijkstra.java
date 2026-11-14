import java.util.Arrays;
import java.util.PriorityQueue;

public class Dijkstra {
    static int[] shortestDistances(int[][][] adjacency, int source) {
        int[] distance = new int[adjacency.length];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[source] = 0;
        boolean[] settled = new boolean[adjacency.length];
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        queue.add(new int[] {0, source});
        while (!queue.isEmpty()) {
            int v = queue.remove()[1];
            if (settled[v]) {
                continue;
            }
            settled[v] = true;
            for (int[] edge : adjacency[v]) {
                int w = edge[0];
                if (!settled[w] && distance[v] + edge[1] < distance[w]) {
                    distance[w] = distance[v] + edge[1];
                    queue.add(new int[] {distance[w], w});
                }
            }
        }
        return distance;
    }

    public static void main(String[] args) {
        int[][][] nonNegative = {
            {{1, 4}, {2, 1}},
            {{3, 1}},
            {{1, 2}, {3, 5}},
            {}
        };
        System.out.println("distances " + Arrays.toString(shortestDistances(nonNegative, 0)));

        int[][][] negativeEdge = {
            {{1, 2}, {2, 3}},
            {},
            {{1, -2}}
        };
        System.out.println("with a negative edge " + Arrays.toString(shortestDistances(negativeEdge, 0)));
    }
}
