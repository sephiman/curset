import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionException;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

public class CompletableFutureFlow {
    public static void main(String[] args) throws Exception {
        AtomicInteger sequence = new AtomicInteger();
        ExecutorService pool = Executors.newFixedThreadPool(2, task -> new Thread(task, "billing-" + sequence.incrementAndGet()));
        try {
            CompletableFuture<String> named = CompletableFuture.supplyAsync(() -> Thread.currentThread().getName(), pool);
            System.out.println("runs on a billing thread: " + named.join().startsWith("billing-"));

            CompletableFuture<Integer> failing = CompletableFuture.supplyAsync(() -> {
                throw new IllegalStateException("tariff missing");
            }, pool);
            try {
                failing.join();
            } catch (CompletionException e) {
                System.out.println("join throws " + e.getClass().getSimpleName() + " caused by " + e.getCause());
            }
            try {
                failing.get();
            } catch (ExecutionException e) {
                System.out.println("get throws " + e.getClass().getSimpleName() + " caused by " + e.getCause());
            }
            System.out.println(failing.exceptionally(error -> -1).join());
            System.out.println(failing.handle((value, error) -> error == null ? "ok" : "failed").join());
            System.out.println(failing.isCompletedExceptionally());

            CompletableFuture<Integer> cancelled = new CompletableFuture<>();
            cancelled.cancel(true);
            System.out.println(cancelled.isCompletedExceptionally());
        } finally {
            pool.shutdown();
        }
    }
}
