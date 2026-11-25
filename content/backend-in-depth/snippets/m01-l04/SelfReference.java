import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.*;
import org.springframework.transaction.*;
import org.springframework.transaction.annotation.*;
import org.springframework.transaction.support.*;

public class SelfReference {
    static class RecordingManager extends AbstractPlatformTransactionManager {
        protected Object doGetTransaction() { return new Object(); }
        protected void doBegin(Object tx, TransactionDefinition d) { System.out.println("begin"); }
        protected void doCommit(DefaultTransactionStatus s) { System.out.println("commit"); }
        protected void doRollback(DefaultTransactionStatus s) { System.out.println("rollback"); }
    }

    public static class Invoices {
        @Autowired @Lazy Invoices self;
        public void viaThis() { this.audit(); }
        public void viaSelf() { self.audit(); }
        @Transactional
        public void audit() { System.out.println("audit"); }
    }

    @Configuration
    @EnableTransactionManagement
    static class Config {
        @Bean Invoices invoices() { return new Invoices(); }
        @Bean PlatformTransactionManager transactionManager() { return new RecordingManager(); }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            Invoices invoices = context.getBean(Invoices.class);
            System.out.println("-- through this");
            invoices.viaThis();
            System.out.println("-- through the self reference");
            invoices.viaSelf();
        }
    }
}
