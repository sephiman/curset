import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ForkJoinPool;

public class CommonPoolDefault {
    public static void main(String[] args) {
        String threadName = CompletableFuture.supplyAsync(() -> Thread.currentThread().getName()).join();
        System.out.println(threadName.startsWith("ForkJoinPool.commonPool-worker-"));

        boolean daemon = CompletableFuture.supplyAsync(() -> Thread.currentThread().isDaemon()).join();
        System.out.println(daemon);

        ForkJoinPool.commonPool().shutdown();
        System.out.println(ForkJoinPool.commonPool().isShutdown());

        String afterShutdown = CompletableFuture.supplyAsync(() -> "still runs").join();
        System.out.println(afterShutdown);
    }
}
