import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class LinkedStructures {
    static class Node {
        final int value;
        Node next;

        Node(int value, Node next) {
            this.value = value;
            this.next = next;
        }
    }

    static Node of(int... values) {
        Node head = null;
        for (int i = values.length - 1; i >= 0; i--) {
            head = new Node(values[i], head);
        }
        return head;
    }

    static Node reverse(Node head) {
        Node previous = null;
        while (head != null) {
            Node next = head.next;
            head.next = previous;
            previous = head;
            head = next;
        }
        return previous;
    }

    static Node middle(Node head) {
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    static boolean hasCycle(Node head) {
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }

    static String show(Node head) {
        StringBuilder text = new StringBuilder();
        for (Node node = head; node != null; node = node.next) {
            text.append(node.value);
        }
        return text.toString();
    }

    static int[] nextGreater(int[] values) {
        int[] result = new int[values.length];
        Arrays.fill(result, -1);
        Deque<Integer> waiting = new ArrayDeque<>();
        for (int i = 0; i < values.length; i++) {
            while (!waiting.isEmpty() && values[waiting.peek()] < values[i]) {
                result[waiting.pop()] = values[i];
            }
            waiting.push(i);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("reversed " + show(reverse(of(1, 2, 3, 4, 5))));
        System.out.println("middle of five " + middle(of(1, 2, 3, 4, 5)).value);
        System.out.println("middle of four " + middle(of(1, 2, 3, 4)).value);

        Node looping = of(1, 2, 3);
        looping.next.next.next = looping.next;
        System.out.println("cycle found " + hasCycle(looping));
        System.out.println("cycle found in a plain list " + hasCycle(of(1, 2, 3)));

        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println("stack contents " + stack);
        System.out.println("stack pop " + stack.pop());

        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
        System.out.println("queue poll " + queue.poll());

        System.out.println("next greater " + Arrays.toString(nextGreater(new int[] {2, 1, 2, 4, 3})));
    }
}
