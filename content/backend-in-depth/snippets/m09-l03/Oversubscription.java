import java.util.Locale;
import java.util.Map;

public class Oversubscription {
    public static void main(String[] args) {
        long capacityCpuSeconds = 10_000;
        Map<String, Long> limits = new java.util.LinkedHashMap<>();
        limits.put("Gmail", 4_000L);
        limits.put("Calendar", 4_000L);
        limits.put("Android", 3_000L);
        limits.put("Google+", 2_000L);
        limits.put("Every other user", 500L);

        long sum = limits.values().stream().mapToLong(Long::longValue).sum();
        System.out.println("capacity CPU seconds per second: " + capacityCpuSeconds);
        System.out.println("sum of per-customer limits: " + sum);
        System.out.println(String.format(Locale.ROOT, "limits as a share of capacity: %.2f", (double) sum / capacityCpuSeconds));
        System.out.println("limits add up to more than capacity: " + (sum > capacityCpuSeconds));
    }
}
