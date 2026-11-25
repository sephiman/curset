import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

public class BfsDistances {
    static int[] distances(List<List<Integer>> adjacency, int start) {
        int[] distance = new int[adjacency.size()];
        Arrays.fill(distance, -1);
        distance[start] = 0;
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        while (!queue.isEmpty()) {
            int v = queue.remove();
            for (int w : adjacency.get(v)) {
                if (distance[w] < 0) {
                    distance[w] = distance[v] + 1;
                    queue.add(w);
                }
            }
        }
        return distance;
    }

    public static void main(String[] args) {
        List<List<Integer>> adjacency = List.of(
            List.of(1, 2), List.of(0, 3), List.of(0, 3), List.of(1, 2, 4), List.of(3), List.of(6), List.of(5));
        System.out.println("distances " + Arrays.toString(distances(adjacency, 0)));
    }
}
