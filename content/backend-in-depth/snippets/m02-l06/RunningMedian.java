import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

public class RunningMedian {
    private final PriorityQueue<Integer> lower = new PriorityQueue<>(Collections.reverseOrder());
    private final PriorityQueue<Integer> upper = new PriorityQueue<>();

    void add(int value) {
        if (lower.isEmpty() || value <= lower.peek()) {
            lower.add(value);
        } else {
            upper.add(value);
        }
        if (lower.size() > upper.size() + 1) {
            upper.add(lower.poll());
        } else if (upper.size() > lower.size()) {
            lower.add(upper.poll());
        }
    }

    double median() {
        return lower.size() > upper.size() ? lower.peek() : (lower.peek() + upper.peek()) / 2.0;
    }

    public static void main(String[] args) {
        RunningMedian stream = new RunningMedian();
        List<Double> medians = new ArrayList<>();
        for (int value : new int[] {5, 15, 1, 3}) {
            stream.add(value);
            medians.add(stream.median());
        }
        System.out.println("medians " + medians);
    }
}
