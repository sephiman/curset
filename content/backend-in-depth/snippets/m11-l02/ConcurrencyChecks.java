import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.atomic.AtomicInteger;

public class ConcurrencyChecks {
    interface Insert {
        boolean insertIfAbsent(Map<String, String> map, CyclicBarrier barrier) throws Exception;
    }

    static int inserts(Insert strategy) throws Exception {
        Map<String, String> map = new ConcurrentHashMap<>();
        CyclicBarrier barrier = new CyclicBarrier(2);
        AtomicInteger inserted = new AtomicInteger();
        Runnable task = () -> {
            try {
                if (strategy.insertIfAbsent(map, barrier)) {
                    inserted.incrementAndGet();
                }
            } catch (Exception e) {
                throw new IllegalStateException(e);
            }
        };
        Thread first = new Thread(task);
        Thread second = new Thread(task);
        first.start();
        second.start();
        first.join();
        second.join();
        return inserted.get();
    }

    public static void main(String[] args) throws Exception {
        System.out.println("check then act: " + inserts((map, barrier) -> {
            boolean absent = !map.containsKey("key");
            barrier.await();
            if (absent) {
                map.put("key", "value");
            }
            return absent;
        }));
        System.out.println("atomic insert: " + inserts((map, barrier) -> {
            barrier.await();
            return map.putIfAbsent("key", "value") == null;
        }));

        int[] box = new int[1];
        Thread writer = new Thread(() -> box[0] = 42);
        writer.start();
        writer.join();
        System.out.println("after join: " + box[0]);
    }
}
