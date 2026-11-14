import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;
import java.util.concurrent.atomic.LongAdder;

public class AtomicCounters {
    public static void main(String[] args) throws InterruptedException {
        AtomicInteger counter = new AtomicInteger();
        LongAdder adder = new LongAdder();
        Thread[] threads = new Thread[4];
        for (int i = 0; i < threads.length; i++) {
            threads[i] = new Thread(() -> {
                for (int n = 0; n < 10_000; n++) {
                    counter.incrementAndGet();
                    adder.increment();
                }
            });
            threads[i].start();
        }
        for (Thread thread : threads) {
            thread.join();
        }
        System.out.println(counter.get() + " " + adder.sum());
        System.out.println(counter.compareAndSet(40_000, 1) + " " + counter.compareAndSet(40_000, 2) + " " + counter.get());
        System.out.println(counter.getAndUpdate(value -> value + 10) + " " + counter.get());
        AtomicReference<String> owner = new AtomicReference<>("none");
        System.out.println(owner.compareAndSet("none", "alice") + " " + owner.compareAndSet("none", "bob") + " " + owner.get());
    }
}
