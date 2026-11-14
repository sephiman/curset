import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class BinarySearchResults {
    static int smallestCapacity(int[] weights, int days) {
        int low = Arrays.stream(weights).max().getAsInt();
        int high = Arrays.stream(weights).sum();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (daysNeeded(weights, mid) <= days) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    static int daysNeeded(int[] weights, int capacity) {
        int days = 1;
        int load = 0;
        for (int weight : weights) {
            if (load + weight > capacity) {
                days++;
                load = 0;
            }
            load += weight;
        }
        return days;
    }

    public static void main(String[] args) {
        int[] sorted = {1, 3, 5, 7, 9};
        System.out.println("found 7 at " + Arrays.binarySearch(sorted, 7));
        System.out.println("missing 6 gives " + Arrays.binarySearch(sorted, 6));
        System.out.println("missing 10 gives " + Arrays.binarySearch(sorted, 10));

        List<Integer> linked = new LinkedList<>(List.of(1, 3, 5, 7, 9));
        System.out.println("linked list finds 3 at " + Collections.binarySearch(linked, 3));

        System.out.println("smallest capacity " + smallestCapacity(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5));

        int low = 1_500_000_000;
        int high = 2_000_000_000;
        System.out.println("overflowing mid " + (low + high) / 2);
        System.out.println("unsigned shift mid " + ((low + high) >>> 1));
        System.out.println("safe mid " + (low + (high - low) / 2));
    }
}
