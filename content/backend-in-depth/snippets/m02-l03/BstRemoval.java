public class BstRemoval {
    record Node(int key, Node left, Node right) {}

    static Node insert(Node node, int key) {
        if (node == null) {
            return new Node(key, null, null);
        }
        Node left = key < node.key() ? insert(node.left(), key) : node.left();
        Node right = key > node.key() ? insert(node.right(), key) : node.right();
        return new Node(node.key(), left, right);
    }

    static int smallest(Node node) {
        return node.left() == null ? node.key() : smallest(node.left());
    }

    static Node remove(Node node, int key) {
        if (key < node.key()) {
            return new Node(node.key(), remove(node.left(), key), node.right());
        }
        if (key > node.key()) {
            return new Node(node.key(), node.left(), remove(node.right(), key));
        }
        if (node.left() == null || node.right() == null) {
            return node.left() == null ? node.right() : node.left();
        }
        int next = smallest(node.right());
        return new Node(next, node.left(), remove(node.right(), next));
    }

    public static void main(String[] args) {
        Node tree = null;
        for (int key : new int[] {8, 3, 10, 1, 6, 14, 4, 7, 13}) {
            tree = insert(tree, key);
        }
        Node left = remove(tree, 3).left();
        System.out.println("left child of the root " + left.key() + ", children " + left.left().key() + " and " + left.right().key());
    }
}
