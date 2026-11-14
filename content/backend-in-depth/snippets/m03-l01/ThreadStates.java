import java.util.concurrent.CountDownLatch;

public class ThreadStates {
    static final Object monitor = new Object();

    static void awaitState(Thread thread, Thread.State wanted) throws InterruptedException {
        while (thread.getState() != wanted) {
            Thread.sleep(5);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        CountDownLatch release = new CountDownLatch(1);
        Thread waiting = new Thread(() -> {
            try {
                release.await();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        Thread sleeping = new Thread(() -> {
            try {
                Thread.sleep(60_000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        Thread blocked = new Thread(() -> {
            synchronized (monitor) {
                System.out.println("blocked thread entered the monitor");
            }
        });
        System.out.println(blocked.getState());
        synchronized (monitor) {
            waiting.start();
            sleeping.start();
            blocked.start();
            awaitState(waiting, Thread.State.WAITING);
            awaitState(sleeping, Thread.State.TIMED_WAITING);
            awaitState(blocked, Thread.State.BLOCKED);
            System.out.println(waiting.getState());
            System.out.println(sleeping.getState());
            System.out.println(blocked.getState());
        }
        blocked.join();
        release.countDown();
        sleeping.interrupt();
        waiting.join();
        sleeping.join();
        System.out.println(waiting.getState());
    }
}
