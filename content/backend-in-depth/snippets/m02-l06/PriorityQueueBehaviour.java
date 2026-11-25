import java.util.Arrays;
import java.util.PriorityQueue;

public class PriorityQueueBehaviour {
    public static void main(String[] args) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        System.out.println("peek when empty: " + queue.peek());
        System.out.println("poll when empty: " + queue.poll());
        queue.add(5);
        queue.add(1);
        queue.add(3);
        System.out.println("peek leaves the head: " + queue.peek() + " of " + queue.size());
        System.out.println("poll removes the head: " + queue.poll() + " of " + queue.size());
        try {
            queue.add(null);
        } catch (NullPointerException e) {
            System.out.println("null element: null pointer");
        }
        Object[] ordered = queue.toArray();
        Arrays.sort(ordered);
        System.out.println("sorted copy " + Arrays.toString(ordered));
    }
}
