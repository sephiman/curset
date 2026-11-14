import java.util.Arrays;
import java.util.Comparator;

public class GreedyChoices {
    static int scheduled(int[][] classes, Comparator<int[]> order) {
        int[][] sorted = classes.clone();
        Arrays.sort(sorted, order);
        int count = 0;
        int lastFinish = Integer.MIN_VALUE;
        for (int[] c : sorted) {
            if (c[0] >= lastFinish) {
                count++;
                lastFinish = c[1];
            }
        }
        return count;
    }

    static int greedyKnapsack(int[] weights, int[] values, int capacity) {
        Integer[] byRatio = new Integer[weights.length];
        for (int i = 0; i < byRatio.length; i++) {
            byRatio[i] = i;
        }
        Arrays.sort(byRatio, Comparator.comparingDouble((Integer i) -> (double) values[i] / weights[i]).reversed());
        int total = 0;
        for (int i : byRatio) {
            if (weights[i] <= capacity) {
                capacity -= weights[i];
                total += values[i];
            }
        }
        return total;
    }

    public static void main(String[] args) {
        int[][] classes = {{1, 10}, {2, 3}, {4, 5}, {6, 7}};
        System.out.println("earliest start " + scheduled(classes, Comparator.comparingInt(c -> c[0])));
        System.out.println("earliest finish " + scheduled(classes, Comparator.comparingInt(c -> c[1])));
        System.out.println("greedy knapsack " + greedyKnapsack(new int[] {1, 3, 4, 5}, new int[] {1, 4, 5, 7}, 7));
    }
}
