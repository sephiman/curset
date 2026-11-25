import java.util.ArrayList;
import java.util.List;

public class TokenBucketBurst {
    private final long capacity;
    private final long refillPerSecond;
    private long tokens;
    private long lastSecond;

    TokenBucketBurst(long capacity, long refillPerSecond) {
        this.capacity = capacity;
        this.refillPerSecond = refillPerSecond;
        this.tokens = capacity;
    }

    boolean tryAcquire(long second) {
        tokens = Math.min(capacity, tokens + (second - lastSecond) * refillPerSecond);
        lastSecond = second;
        if (tokens == 0) {
            return false;
        }
        tokens--;
        return true;
    }

    static List<Boolean> requests(TokenBucketBurst bucket, long second, int count) {
        List<Boolean> results = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            results.add(bucket.tryAcquire(second));
        }
        return results;
    }

    public static void main(String[] args) {
        TokenBucketBurst bucket = new TokenBucketBurst(3, 1);
        System.out.println("at second 0: " + requests(bucket, 0, 4));
        System.out.println("at second 1: " + requests(bucket, 1, 2));
        System.out.println("at second 100: " + requests(bucket, 100, 5));
    }
}
