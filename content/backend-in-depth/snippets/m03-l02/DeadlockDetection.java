import java.lang.management.ManagementFactory;
import java.util.Arrays;
import java.util.concurrent.CountDownLatch;

public class DeadlockDetection {
    static final Object first = new Object();
    static final Object second = new Object();

    static Thread worker(String name, Object held, Object wanted, CountDownLatch bothHold) {
        Thread thread = new Thread(() -> {
            synchronized (held) {
                bothHold.countDown();
                try {
                    bothHold.await();
                } catch (InterruptedException e) {
                    return;
                }
                synchronized (wanted) {
                    System.out.println(name + " got both locks");
                }
            }
        }, name);
        thread.setDaemon(true);
        return thread;
    }

    public static void main(String[] args) throws InterruptedException {
        CountDownLatch bothHold = new CountDownLatch(2);
        worker("worker-A", first, second, bothHold).start();
        worker("worker-B", second, first, bothHold).start();
        long[] ids = null;
        while (ids == null) {
            Thread.sleep(20);
            ids = ManagementFactory.getThreadMXBean().findDeadlockedThreads();
        }
        String[] names = Arrays.stream(ManagementFactory.getThreadMXBean().getThreadInfo(ids))
                .map(info -> info.getThreadName() + " is " + info.getThreadState())
                .sorted()
                .toArray(String[]::new);
        System.out.println(ids.length + " deadlocked threads: " + String.join(", ", names));
    }
}
