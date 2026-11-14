import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.StampedLock;

public class LockModes {
    public static void main(String[] args) {
        ReentrantLock lock = new ReentrantLock();
        lock.lock();
        lock.lock();
        System.out.println("hold count " + lock.getHoldCount() + ", held " + lock.isHeldByCurrentThread());
        lock.unlock();
        lock.unlock();
        System.out.println("hold count " + lock.getHoldCount() + ", locked " + lock.isLocked());

        StampedLock stamped = new StampedLock();
        long optimistic = stamped.tryOptimisticRead();
        System.out.println("nonzero stamp " + (optimistic != 0L) + ", valid " + stamped.validate(optimistic));
        long write = stamped.writeLock();
        stamped.unlockWrite(write);
        System.out.println("valid after a write " + stamped.validate(optimistic));
        long writeAgain = stamped.writeLock();
        System.out.println("optimistic stamp while writing " + stamped.tryOptimisticRead());
        stamped.unlockWrite(writeAgain);

        Semaphore permits = new Semaphore(2);
        System.out.println(permits.tryAcquire() + " " + permits.tryAcquire() + " " + permits.tryAcquire());
        permits.release();
        System.out.println("available " + permits.availablePermits());
    }
}
