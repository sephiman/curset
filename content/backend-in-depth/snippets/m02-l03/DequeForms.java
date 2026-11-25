import java.util.ArrayDeque;
import java.util.Deque;
import java.util.NoSuchElementException;

public class DequeForms {
    public static void main(String[] args) {
        Deque<Integer> empty = new ArrayDeque<>();
        System.out.println("poll form on empty " + empty.pollFirst());
        System.out.println("peek form on empty " + empty.peekFirst());
        try {
            empty.removeFirst();
        } catch (NoSuchElementException e) {
            System.out.println("throwing form on empty: exception");
        }

        Deque<Integer> stack = new ArrayDeque<>();
        Deque<Integer> queue = new ArrayDeque<>();
        for (int value = 1; value <= 3; value++) {
            stack.push(value);
            queue.offerLast(value);
        }
        System.out.println("stack peek " + stack.peek() + ", queue peek " + queue.peek());
        System.out.println("stack first " + stack.peekFirst() + ", queue first " + queue.peekFirst());
        System.out.println("stack " + stack + ", queue " + queue);
    }
}
