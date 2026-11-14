public class InterruptStatus {
    public static void main(String[] args) {
        Thread.currentThread().interrupt();
        System.out.println(Thread.interrupted());
        System.out.println(Thread.interrupted());

        Thread.currentThread().interrupt();
        try {
            Thread.sleep(10);
        } catch (InterruptedException swallowed) {
            System.out.println("caught, status " + Thread.currentThread().isInterrupted());
        }

        Thread.currentThread().interrupt();
        try {
            Thread.sleep(10);
        } catch (InterruptedException restored) {
            Thread.currentThread().interrupt();
            System.out.println("caught, status " + Thread.currentThread().isInterrupted());
        }
    }
}
