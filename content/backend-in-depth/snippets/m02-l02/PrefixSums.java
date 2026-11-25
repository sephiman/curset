import java.util.Arrays;

public class PrefixSums {
    public static void main(String[] args) {
        long[] values = {2, 1, 0, 3};
        Arrays.parallelPrefix(values, Long::sum);
        System.out.println("prefix sums " + Arrays.toString(values));
        System.out.println("sum of the last two " + (values[3] - values[1]));
    }
}
