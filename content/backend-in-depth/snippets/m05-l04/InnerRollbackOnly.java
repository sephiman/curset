import org.springframework.transaction.*;
import org.springframework.transaction.support.*;

public class InnerRollbackOnly {
    static class Tx implements SmartTransactionObject {
        boolean rollbackOnly;
        public boolean isRollbackOnly() { return rollbackOnly; }
        public void flush() { }
    }
    static class RecordingManager extends AbstractPlatformTransactionManager {
        private Tx current;
        protected Object doGetTransaction() { return current == null ? new Tx() : current; }
        protected boolean isExistingTransaction(Object tx) { return current != null; }
        protected Object doSuspend(Object tx) { Tx outer = current; current = null; return outer; }
        protected void doResume(Object tx, Object outer) { current = (Tx) outer; }
        protected void doBegin(Object tx, TransactionDefinition d) { current = (Tx) tx; System.out.println("begin"); }
        protected void doCommit(DefaultTransactionStatus s) { System.out.println("commit"); current = null; }
        protected void doRollback(DefaultTransactionStatus s) { System.out.println("rollback"); current = null; }
        protected void doSetRollbackOnly(DefaultTransactionStatus s) { ((Tx) s.getTransaction()).rollbackOnly = true; }
    }
    static void run(PlatformTransactionManager manager, String name, int propagation) {
        System.out.println("-- inner " + name + " marks rollback-only");
        TransactionTemplate inner = new TransactionTemplate(manager);
        inner.setPropagationBehavior(propagation);
        try {
            new TransactionTemplate(manager).executeWithoutResult(
                outer -> inner.executeWithoutResult(status -> status.setRollbackOnly()));
            System.out.println("outer returned normally");
        } catch (UnexpectedRollbackException e) {
            System.out.println("outer failed: unexpected rollback");
        }
    }
    public static void main(String[] args) {
        PlatformTransactionManager manager = new RecordingManager();
        run(manager, "required", TransactionDefinition.PROPAGATION_REQUIRED);
        run(manager, "requires new", TransactionDefinition.PROPAGATION_REQUIRES_NEW);
    }
}
