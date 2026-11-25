import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class IntervalMerge {
    public static void main(String[] args) {
        int[][] intervals = {{1, 4}, {2, 6}, {8, 10}, {5, 9}, {12, 13}};
        Arrays.sort(intervals, Comparator.comparingInt(interval -> interval[0]));
        List<int[]> merged = new ArrayList<>();
        for (int[] interval : intervals) {
            if (!merged.isEmpty() && interval[0] <= merged.getLast()[1]) {
                merged.getLast()[1] = Math.max(merged.getLast()[1], interval[1]);
            } else {
                merged.add(interval.clone());
            }
        }
        merged.forEach(interval -> System.out.println("merged " + Arrays.toString(interval)));
    }
}
