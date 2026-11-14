public class VolatileHandoff {
    static int payload;
    static volatile boolean ready;

    public static void main(String[] args) throws InterruptedException {
        Thread writer = new Thread(() -> {
            payload = 42;
            ready = true;
        });
        writer.start();
        while (!ready) {
            Thread.onSpinWait();
        }
        System.out.println("payload after the volatile read: " + payload);
        writer.join();
        System.out.println("writer alive after join: " + writer.isAlive());
    }
}
