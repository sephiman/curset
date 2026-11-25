import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class ExplicitStackDfs {
    static List<Integer> order(List<List<Integer>> adjacency, int start) {
        List<Integer> order = new ArrayList<>();
        boolean[] seen = new boolean[adjacency.size()];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(start);
        while (!stack.isEmpty()) {
            int v = stack.pop();
            if (!seen[v]) {
                seen[v] = true;
                order.add(v);
                for (int w : adjacency.get(v)) {
                    stack.push(w);
                }
            }
        }
        return order;
    }

    public static void main(String[] args) {
        List<List<Integer>> adjacency = List.of(
            List.of(1, 2), List.of(0, 3), List.of(0, 3), List.of(1, 2, 4), List.of(3), List.of(6), List.of(5));
        System.out.println("explicit stack " + order(adjacency, 0));
    }
}
