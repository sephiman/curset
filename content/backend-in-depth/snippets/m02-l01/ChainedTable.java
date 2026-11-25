import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Stream;

public class ChainedTable {
    private List<LinkedList<Integer>> buckets = emptyBuckets(16);
    private int size;

    private static List<LinkedList<Integer>> emptyBuckets(int count) {
        return new ArrayList<>(Stream.generate(() -> new LinkedList<Integer>()).limit(count).toList());
    }

    private void place(int key) {
        buckets.get(Math.floorMod(key, buckets.size())).add(key);
    }

    void add(int key) {
        place(key);
        size++;
        if (size > 0.75 * buckets.size()) {
            List<LinkedList<Integer>> old = buckets;
            buckets = emptyBuckets(old.size() * 2);
            old.forEach(chain -> chain.forEach(this::place));
        }
    }

    public static void main(String[] args) {
        ChainedTable table = new ChainedTable();
        for (int key = 1; key <= 13; key++) {
            table.add(key * 16);
            int longest = table.buckets.stream().mapToInt(List::size).max().getAsInt();
            if (key >= 12) {
                System.out.println(key + " entries, " + table.buckets.size() + " buckets, longest chain " + longest);
            }
        }
    }
}
