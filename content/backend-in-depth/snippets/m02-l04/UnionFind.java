import java.util.Arrays;

public class UnionFind {
    static int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }

    static void union(int[] parent, int a, int b) {
        parent[find(parent, a)] = find(parent, b);
    }

    public static void main(String[] args) {
        int[] parent = {0, 1, 2, 3};
        union(parent, 0, 1);
        union(parent, 1, 2);
        union(parent, 2, 3);
        System.out.println("before " + Arrays.toString(parent));

        find(parent, 0);
        System.out.println("after find(0) " + Arrays.toString(parent));

        long leaders = java.util.stream.IntStream.range(0, parent.length).filter(x -> parent[x] == x).count();
        System.out.println("components " + leaders);
    }
}
