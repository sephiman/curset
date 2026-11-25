import java.io.IOException;
import org.springframework.context.annotation.*;
import org.springframework.transaction.*;
import org.springframework.transaction.annotation.*;
import org.springframework.transaction.support.*;

public class RollbackRules {
    static class RecordingManager extends AbstractPlatformTransactionManager {
        protected Object doGetTransaction() { return new Object(); }
        protected void doBegin(Object tx, TransactionDefinition d) { }
        protected void doCommit(DefaultTransactionStatus s) { System.out.println("  commit"); }
        protected void doRollback(DefaultTransactionStatus s) { System.out.println("  rollback"); }
    }
    public static class Ledger {
        @Transactional public void unchecked() { throw new IllegalStateException(); }
        @Transactional public void checked() throws IOException { throw new IOException(); }
        @Transactional(rollbackFor = IOException.class) public void checkedWithRule() throws IOException { throw new IOException(); }
        @Transactional(noRollbackFor = IllegalStateException.class) public void uncheckedWithRule() { throw new IllegalStateException(); }
    }
    @Configuration @EnableTransactionManagement
    static class Config {
        @Bean Ledger ledger() { return new Ledger(); }
        @Bean PlatformTransactionManager transactionManager() { return new RecordingManager(); }
    }
    interface Call { void run() throws Exception; }
    static void call(String name, Call call) {
        System.out.println(name);
        try { call.run(); } catch (Exception e) { System.out.println("  thrown " + (e instanceof RuntimeException ? "unchecked" : "checked") + " exception"); }
    }
    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            Ledger ledger = context.getBean(Ledger.class);
            call("unchecked", ledger::unchecked);
            call("checked", ledger::checked);
            call("checked, with a rollback rule", ledger::checkedWithRule);
            call("unchecked, with a no-rollback rule", ledger::uncheckedWithRule);
        }
    }
}
