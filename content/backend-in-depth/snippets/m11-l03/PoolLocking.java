import java.util.concurrent.CountDownLatch;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class PoolLocking {
    static int threadsThatFinish(int poolSize, int threads, int connectionsPerThread) throws Exception {
        Semaphore pool = new Semaphore(poolSize);
        CyclicBarrier allHoldAllButOne = new CyclicBarrier(threads);
        CountDownLatch outcomes = new CountDownLatch(threads);
        AtomicInteger finished = new AtomicInteger();
        Thread[] workers = new Thread[threads];
        for (int i = 0; i < threads; i++) {
            workers[i] = new Thread(() -> {
                try {
                    int held = connectionsPerThread - 1;
                    pool.acquire(held);
                    allHoldAllButOne.await();
                    boolean gotLast = pool.tryAcquire(500, TimeUnit.MILLISECONDS);
                    if (gotLast) {
                        finished.incrementAndGet();
                        held++;
                    }
                    outcomes.countDown();
                    if (!gotLast) {
                        outcomes.await();
                    }
                    pool.release(held);
                } catch (Exception e) {
                    throw new IllegalStateException(e);
                }
            });
            workers[i].start();
        }
        for (Thread worker : workers) {
            worker.join();
        }
        return finished.get();
    }

    public static void main(String[] args) throws Exception {
        int threads = 3;
        int connectionsPerThread = 4;
        int minimum = threads * (connectionsPerThread - 1) + 1;
        System.out.println("minimum pool " + minimum);
        System.out.println("pool " + (minimum - 1) + ": " + threadsThatFinish(minimum - 1, threads, connectionsPerThread) + " of 3 finish");
        System.out.println("pool " + minimum + ": " + threadsThatFinish(minimum, threads, connectionsPerThread) + " of 3 finish");
    }
}
