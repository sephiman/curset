import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.RejectedExecutionException;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class BoundedPool {
    public static void main(String[] args) throws InterruptedException {
        CountDownLatch release = new CountDownLatch(1);
        ThreadPoolExecutor pool = new ThreadPoolExecutor(1, 1, 0L, TimeUnit.SECONDS, new ArrayBlockingQueue<>(1));
        Runnable blocking = () -> {
            try {
                release.await();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        };
        pool.execute(blocking);
        pool.execute(blocking);
        System.out.println("pool size " + pool.getPoolSize() + ", queued " + pool.getQueue().size());
        try {
            pool.execute(blocking);
        } catch (RejectedExecutionException e) {
            System.out.println("third task: " + e.getClass().getSimpleName());
        }
        release.countDown();
        pool.shutdown();
        System.out.println("terminated: " + pool.awaitTermination(5, TimeUnit.SECONDS));
        System.out.println("completed tasks: " + pool.getCompletedTaskCount());
    }
}
