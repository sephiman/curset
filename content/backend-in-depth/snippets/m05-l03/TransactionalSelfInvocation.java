import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.transaction.*;
import org.springframework.transaction.annotation.*;
import org.springframework.transaction.support.*;

public class TransactionalSelfInvocation {
    static class RecordingManager extends AbstractPlatformTransactionManager {
        protected Object doGetTransaction() { return new Object(); }
        protected void doBegin(Object tx, TransactionDefinition d) { System.out.println("begin"); }
        protected void doCommit(DefaultTransactionStatus s) { System.out.println("commit"); }
        protected void doRollback(DefaultTransactionStatus s) { System.out.println("rollback"); }
    }

    public static class Orders {
        public void placeOrder() { System.out.println("place order"); this.audit(); }
        @Transactional(propagation = Propagation.REQUIRES_NEW)
        public void audit() { System.out.println("audit"); }
    }

    @Configuration @EnableTransactionManagement
    static class Config {
        @Bean Orders orders() { return new Orders(); }
        @Bean PlatformTransactionManager transactionManager() { return new RecordingManager(); }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            Orders orders = context.getBean(Orders.class);
            System.out.println("-- self-invocation");
            orders.placeOrder();
            System.out.println("-- through the proxy");
            orders.audit();
        }
    }
}
