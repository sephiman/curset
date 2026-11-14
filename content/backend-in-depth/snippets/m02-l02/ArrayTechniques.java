import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class ArrayTechniques {
    static int[] pairWithSum(int[] sorted, int target) {
        int left = 0;
        int right = sorted.length - 1;
        while (left < right) {
            int sum = sorted[left] + sorted[right];
            if (sum == target) {
                return new int[] {left, right};
            }
            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[] {-1, -1};
    }

    static int maxWindowSum(int[] values, int width) {
        int window = 0;
        for (int i = 0; i < width; i++) {
            window += values[i];
        }
        int best = window;
        for (int i = width; i < values.length; i++) {
            window += values[i] - values[i - width];
            best = Math.max(best, window);
        }
        return best;
    }

    static int countSubarraysWithSum(int[] values, int target) {
        Map<Integer, Integer> seenPrefixes = new HashMap<>();
        seenPrefixes.put(0, 1);
        int prefix = 0;
        int count = 0;
        for (int value : values) {
            prefix += value;
            count += seenPrefixes.getOrDefault(prefix - target, 0);
            seenPrefixes.merge(prefix, 1, Integer::sum);
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println("pair indices " + Arrays.toString(pairWithSum(new int[] {1, 3, 4, 6, 8, 11}, 10)));
        System.out.println("max window sum " + maxWindowSum(new int[] {2, 1, 5, 1, 3, 2}, 3));

        int[] values = {3, 1, 4, 1, 5, 9, 2, 6};
        long[] prefix = new long[values.length + 1];
        for (int i = 0; i < values.length; i++) {
            prefix[i + 1] = prefix[i] + values[i];
        }
        System.out.println("range sum " + (prefix[6] - prefix[2]));

        System.out.println("subarrays with sum 2: " + countSubarraysWithSum(new int[] {1, 1, 1}, 2));

        Map<Character, Integer> counts = new TreeMap<>();
        for (char c : "mississippi".toCharArray()) {
            counts.merge(c, 1, Integer::sum);
        }
        System.out.println("letter counts " + counts);
    }
}
