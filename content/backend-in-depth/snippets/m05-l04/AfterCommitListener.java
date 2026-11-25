import org.springframework.context.annotation.*;
import org.springframework.transaction.*;
import org.springframework.transaction.annotation.*;
import org.springframework.transaction.event.*;
import org.springframework.transaction.support.*;
public class AfterCommitListener {
    static class RecordingManager extends AbstractPlatformTransactionManager {
        protected Object doGetTransaction() { return new Object(); }
        protected void doBegin(Object tx, TransactionDefinition d) { }
        protected void doCommit(DefaultTransactionStatus s) { System.out.println("  commit"); }
        protected void doRollback(DefaultTransactionStatus s) { System.out.println("  rollback"); }
    }
    public static class Listeners {
        @TransactionalEventListener(phase = TransactionPhase.BEFORE_COMMIT)
        public void beforeCommit(String event) { System.out.println("  before commit: " + event); }
        @TransactionalEventListener
        public void afterCommit(String event) { System.out.println("  after commit: " + event); }
        @TransactionalEventListener(phase = TransactionPhase.AFTER_ROLLBACK)
        public void afterRollback(String event) { System.out.println("  after rollback: " + event); }
        @TransactionalEventListener(fallbackExecution = true)
        public void afterCommitOrNoTransaction(String event) { System.out.println("  fallback: " + event); }
    }
    @Configuration @EnableTransactionManagement
    static class Config {
        @Bean Listeners listeners() { return new Listeners(); }
        @Bean PlatformTransactionManager transactionManager() { return new RecordingManager(); }
    }
    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            TransactionTemplate template = new TransactionTemplate(context.getBean(PlatformTransactionManager.class));
            System.out.println("no transaction");
            context.publishEvent("A");
            System.out.println("commit");
            template.executeWithoutResult(status -> context.publishEvent("B"));
            System.out.println("rollback");
            template.executeWithoutResult(status -> { context.publishEvent("C"); status.setRollbackOnly(); });
        }
    }
}
