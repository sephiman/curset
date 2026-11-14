import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.TreeMap;

public class CollectionContracts {
    public static void main(String[] args) {
        try {
            new ArrayDeque<String>().addLast(null);
        } catch (NullPointerException e) {
            System.out.println("ArrayDeque rejects null");
        }

        try {
            new TreeMap<String, Integer>().putFirst("a", 1);
        } catch (UnsupportedOperationException e) {
            System.out.println("TreeMap.putFirst throws UnsupportedOperationException");
        }

        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int value : new int[] {5, 1, 4, 2, 3}) {
            queue.offer(value);
        }
        List<Integer> polled = new ArrayList<>();
        while (!queue.isEmpty()) {
            polled.add(queue.poll());
        }
        System.out.println(polled);

        PriorityQueue<Integer> reversed = new PriorityQueue<>((x, y) -> Integer.compare(y, x));
        reversed.addAll(List.of(5, 1, 4, 2, 3));
        System.out.println(reversed.poll());
    }
}
