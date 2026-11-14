import java.util.concurrent.Semaphore;

public class SemaphoreLimit {
    public static void main(String[] args) {
        Semaphore permits = new Semaphore(2);
        System.out.println("available=" + permits.availablePermits());
        System.out.println("first=" + permits.tryAcquire());
        System.out.println("second=" + permits.tryAcquire());
        System.out.println("third=" + permits.tryAcquire());
        permits.release();
        System.out.println("after release available=" + permits.availablePermits());
    }
}
