import java.util.HashMap;
import java.util.Map;

public class FibonacciMemoisation {
    static long naiveCalls;
    static long memoisedCalls;

    static long naive(int n) {
        naiveCalls++;
        return n < 2 ? n : naive(n - 1) + naive(n - 2);
    }

    static long memoised(int n, Map<Integer, Long> memo) {
        memoisedCalls++;
        if (n < 2) {
            return n;
        }
        Long known = memo.get(n);
        if (known != null) {
            return known;
        }
        long value = memoised(n - 1, memo) + memoised(n - 2, memo);
        memo.put(n, value);
        return value;
    }

    public static void main(String[] args) {
        System.out.println("fib(20) " + naive(20));
        System.out.println("naive calls " + naiveCalls);
        memoised(20, new HashMap<>());
        System.out.println("memoised calls " + memoisedCalls);
    }
}
