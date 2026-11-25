import org.springframework.transaction.*;
import org.springframework.transaction.support.*;

public class RequiredVersusRequiresNew {
    static class RecordingManager extends AbstractPlatformTransactionManager {
        private final int[] current = {0};
        private int counter;
        protected Object doGetTransaction() { return current; }
        protected boolean isExistingTransaction(Object tx) { return current[0] != 0; }
        protected Object doSuspend(Object tx) { int outer = current[0]; current[0] = 0; return outer; }
        protected void doResume(Object tx, Object outer) { current[0] = (Integer) outer; }
        protected void doBegin(Object tx, TransactionDefinition d) { current[0] = ++counter; System.out.println("begin " + counter); }
        protected void doCommit(DefaultTransactionStatus s) { System.out.println("commit " + current[0]); current[0] = 0; }
        protected void doRollback(DefaultTransactionStatus s) { System.out.println("rollback " + current[0]); current[0] = 0; }
        protected void doSetRollbackOnly(DefaultTransactionStatus s) { }
    }

    static void inner(PlatformTransactionManager manager, int propagation) {
        TransactionTemplate template = new TransactionTemplate(manager);
        template.setPropagationBehavior(propagation);
        template.executeWithoutResult(status -> System.out.println("  inner runs, new transaction: " + status.isNewTransaction()));
    }

    static void run(PlatformTransactionManager manager, String name, int propagation) {
        System.out.println("-- inner " + name);
        new TransactionTemplate(manager).executeWithoutResult(outer -> inner(manager, propagation));
    }

    public static void main(String[] args) {
        PlatformTransactionManager manager = new RecordingManager();
        run(manager, "required", TransactionDefinition.PROPAGATION_REQUIRED);
        run(manager, "requires new", TransactionDefinition.PROPAGATION_REQUIRES_NEW);
    }
}
