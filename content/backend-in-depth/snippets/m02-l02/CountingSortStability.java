import java.util.Arrays;

public class CountingSortStability {
    record Item(int key, String label) {
        @Override
        public String toString() {
            return key + label;
        }
    }

    static Item[] countingSort(Item[] items, int range, boolean backwards) {
        int[] counters = new int[range];
        for (Item item : items) {
            counters[item.key()]++;
        }
        for (int i = 1; i < range; i++) {
            counters[i] += counters[i - 1];
        }
        Item[] output = new Item[items.length];
        for (int n = 0; n < items.length; n++) {
            Item item = items[backwards ? items.length - 1 - n : n];
            output[--counters[item.key()]] = item;
        }
        return output;
    }

    public static void main(String[] args) {
        Item[] items = {new Item(2, "a"), new Item(1, "b"), new Item(2, "c"), new Item(1, "d"), new Item(0, "e")};
        System.out.println("scan backwards " + Arrays.toString(countingSort(items, 3, true)));
        System.out.println("scan forwards " + Arrays.toString(countingSort(items, 3, false)));
    }
}
