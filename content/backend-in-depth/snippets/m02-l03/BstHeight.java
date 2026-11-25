public class BstHeight {
    record Node(int key, Node left, Node right) {
    }

    static Node insert(Node node, int key) {
        if (node == null) {
            return new Node(key, null, null);
        }
        if (key < node.key()) {
            return new Node(node.key(), insert(node.left(), key), node.right());
        }
        return new Node(node.key(), node.left(), insert(node.right(), key));
    }

    static int height(Node node) {
        return node == null ? -1 : 1 + Math.max(height(node.left()), height(node.right()));
    }

    public static void main(String[] args) {
        Node mixed = null;
        for (int key : new int[] {8, 3, 10, 1, 6, 14, 4, 7, 13}) {
            mixed = insert(mixed, key);
        }
        Node chain = null;
        for (int key = 1; key <= 8; key++) {
            chain = insert(chain, key);
        }
        System.out.println("height after inserting 8, 3, 10, 1, 6, 14, 4, 7, 13: " + height(mixed));
        System.out.println("height after inserting 1 to 8 in order: " + height(chain));
    }
}
