import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.Queue;

public class TreeAlgorithms {
    record Node(int value, Node left, Node right) {
    }

    static Node leaf(int value) {
        return new Node(value, null, null);
    }

    static void inorder(Node node, List<Integer> out) {
        if (node == null) {
            return;
        }
        inorder(node.left(), out);
        out.add(node.value());
        inorder(node.right(), out);
    }

    static List<Integer> inorderIterative(Node root) {
        List<Integer> out = new ArrayList<>();
        Deque<Node> path = new ArrayDeque<>();
        Node current = root;
        while (current != null || !path.isEmpty()) {
            while (current != null) {
                path.push(current);
                current = current.left();
            }
            current = path.pop();
            out.add(current.value());
            current = current.right();
        }
        return out;
    }

    static List<List<Integer>> levels(Node root) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<Node> queue = new ArrayDeque<>();
        if (root != null) {
            queue.add(root);
        }
        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            for (int remaining = queue.size(); remaining > 0; remaining--) {
                Node node = queue.remove();
                level.add(node.value());
                if (node.left() != null) {
                    queue.add(node.left());
                }
                if (node.right() != null) {
                    queue.add(node.right());
                }
            }
            result.add(level);
        }
        return result;
    }

    static int lowestCommonAncestorInBst(Node root, int p, int q) {
        Node node = root;
        while (true) {
            if (p < node.value() && q < node.value()) {
                node = node.left();
            } else if (p > node.value() && q > node.value()) {
                node = node.right();
            } else {
                return node.value();
            }
        }
    }

    static boolean localCheck(Node node) {
        if (node == null) {
            return true;
        }
        boolean leftOk = node.left() == null || node.left().value() < node.value();
        boolean rightOk = node.right() == null || node.right().value() > node.value();
        return leftOk && rightOk && localCheck(node.left()) && localCheck(node.right());
    }

    static boolean withinBounds(Node node, long low, long high) {
        if (node == null) {
            return true;
        }
        if (node.value() <= low || node.value() >= high) {
            return false;
        }
        return withinBounds(node.left(), low, node.value()) && withinBounds(node.right(), node.value(), high);
    }

    static int recursiveHeight(Node node) {
        if (node == null) {
            return -1;
        }
        return 1 + Math.max(recursiveHeight(node.left()), recursiveHeight(node.right()));
    }

    public static void main(String[] args) {
        Node tree = new Node(8,
                new Node(3, leaf(1), new Node(6, leaf(4), leaf(7))),
                new Node(10, null, new Node(14, leaf(13), null)));

        List<Integer> recursive = new ArrayList<>();
        inorder(tree, recursive);
        System.out.println("inorder " + recursive);
        System.out.println("iterative inorder " + inorderIterative(tree));
        System.out.println("levels " + levels(tree));
        System.out.println("lca of 4 and 7 " + lowestCommonAncestorInBst(tree, 4, 7));
        System.out.println("lca of 4 and 14 " + lowestCommonAncestorInBst(tree, 4, 14));

        Node invalid = new Node(10, leaf(5), new Node(15, leaf(6), null));
        System.out.println("local check " + localCheck(invalid));
        System.out.println("bounds check " + withinBounds(invalid, Long.MIN_VALUE, Long.MAX_VALUE));

        Node chain = null;
        for (int i = 1_000_000; i >= 1; i--) {
            chain = new Node(i, null, chain);
        }
        try {
            recursiveHeight(chain);
        } catch (StackOverflowError e) {
            System.out.println("recursive height overflows the stack");
        }
        System.out.println("iterative levels " + levels(chain).size());
    }
}
