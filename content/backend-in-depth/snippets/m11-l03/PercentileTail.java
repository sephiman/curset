import java.util.Arrays;

public class PercentileTail {
    static int nearestRank(int[] sorted, double percentile) {
        int rank = (int) Math.ceil(percentile / 100 * sorted.length);
        return sorted[rank - 1];
    }

    public static void main(String[] args) {
        int[] latenciesMs = new int[100];
        Arrays.fill(latenciesMs, 0, 98, 10);
        Arrays.fill(latenciesMs, 98, 100, 1000);
        Arrays.sort(latenciesMs);

        System.out.println("mean " + Arrays.stream(latenciesMs).average().orElseThrow());
        System.out.println("p50 " + nearestRank(latenciesMs, 50));
        System.out.println("p98 " + nearestRank(latenciesMs, 98));
        System.out.println("p99 " + nearestRank(latenciesMs, 99));
    }
}
