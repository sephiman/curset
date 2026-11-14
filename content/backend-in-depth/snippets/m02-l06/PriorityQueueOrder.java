import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class PriorityQueueOrder {
    public static void main(String[] args) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        queue.add(5);
        queue.add(1);
        queue.add(3);
        System.out.println("queue as printed " + queue);

        List<Integer> polled = new ArrayList<>();
        while (!queue.isEmpty()) {
            polled.add(queue.poll());
        }
        System.out.println("queue polled " + polled);
    }
}
