import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

public class GcPauseSums {
    record Pause(int gcId, int millis) {}

    public static void main(String[] args) {
        List<Pause> pauses = List.of(
                new Pause(1, 3), new Pause(1, 1),
                new Pause(2, 2),
                new Pause(3, 10), new Pause(3, 1));

        Map<Integer, Integer> sumPerGc = new TreeMap<>();
        for (Pause pause : pauses) {
            sumPerGc.merge(pause.gcId(), pause.millis(), Integer::sum);
        }

        int total = sumPerGc.values().stream().mapToInt(Integer::intValue).sum();
        int largest = sumPerGc.values().stream().mapToInt(Integer::intValue).max().orElseThrow();
        System.out.println("sum of pauses per GC " + sumPerGc);
        System.out.println("total " + total + " ms");
        System.out.println("largest sum " + largest + " ms");
        System.out.printf(Locale.ROOT, "average sum %.2f ms%n", (double) total / sumPerGc.size());
    }
}
