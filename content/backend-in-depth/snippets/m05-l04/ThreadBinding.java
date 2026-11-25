import org.springframework.transaction.*;
import org.springframework.transaction.support.*;

public class ThreadBinding {
    static class RecordingManager extends AbstractPlatformTransactionManager {
        protected Object doGetTransaction() { return new Object(); }
        protected void doBegin(Object tx, TransactionDefinition d) { }
        protected void doCommit(DefaultTransactionStatus s) { }
        protected void doRollback(DefaultTransactionStatus s) { }
    }

    static boolean activeInNewThread() throws InterruptedException {
        boolean[] seen = new boolean[1];
        Thread thread = new Thread(() -> seen[0] = TransactionSynchronizationManager.isActualTransactionActive());
        thread.start();
        thread.join();
        return seen[0];
    }

    public static void main(String[] args) {
        System.out.println("before: " + TransactionSynchronizationManager.isActualTransactionActive());
        new TransactionTemplate(new RecordingManager()).executeWithoutResult(status -> {
            System.out.println("inside, same thread: " + TransactionSynchronizationManager.isActualTransactionActive());
            try {
                System.out.println("inside, new thread: " + activeInNewThread());
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        System.out.println("after: " + TransactionSynchronizationManager.isActualTransactionActive());
    }
}
