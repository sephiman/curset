import java.util.Arrays;

public class HeapArray {
    static final int[] items = new int[16];
    static int size;

    static void swap(int a, int b) {
        int held = items[a];
        items[a] = items[b];
        items[b] = held;
    }

    static void add(int value) {
        items[size++] = value;
        for (int i = size - 1; i > 0 && items[i] < items[(i - 1) / 2]; i = (i - 1) / 2) {
            swap(i, (i - 1) / 2);
        }
    }

    static void trickleDown(int i) {
        int child = 2 * i + 1;
        if (child + 1 < size && items[child + 1] < items[child]) {
            child++;
        }
        if (child < size && items[child] < items[i]) {
            swap(i, child);
            trickleDown(child);
        }
    }

    public static void main(String[] args) {
        Arrays.stream(new int[] {5, 3, 8, 1, 4}).forEach(HeapArray::add);
        System.out.println("after adding 5, 3, 8, 1, 4: " + Arrays.toString(Arrays.copyOf(items, size)));
        items[0] = items[--size];
        trickleDown(0);
        System.out.println("after removing the root: " + Arrays.toString(Arrays.copyOf(items, size)));
    }
}
