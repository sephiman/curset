import org.springframework.context.ApplicationEventPublisher;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.event.EventListener;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.TransactionDefinition;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.event.TransactionalEventListener;
import org.springframework.transaction.support.AbstractPlatformTransactionManager;
import org.springframework.transaction.support.DefaultTransactionStatus;

public class OrderEvents {
    record OrderCompleted(long orderId) {}

    static class RecordingManager extends AbstractPlatformTransactionManager {
        protected Object doGetTransaction() { return new Object(); }
        protected void doBegin(Object tx, TransactionDefinition d) { System.out.println("begin"); }
        protected void doCommit(DefaultTransactionStatus s) { System.out.println("commit"); }
        protected void doRollback(DefaultTransactionStatus s) { System.out.println("rollback"); }
    }

    public static class OrderManagement {
        private final ApplicationEventPublisher events;
        OrderManagement(ApplicationEventPublisher events) { this.events = events; }

        @Transactional
        public void complete(long orderId) {
            System.out.println("publishing");
            events.publishEvent(new OrderCompleted(orderId));
            System.out.println("published");
        }
    }

    public static class InventoryManagement {
        @EventListener
        void immediately(OrderCompleted event) { System.out.println("listener, order " + event.orderId()); }

        @TransactionalEventListener
        void afterCommit(OrderCompleted event) { System.out.println("after-commit listener, order " + event.orderId()); }
    }

    @Configuration
    @EnableTransactionManagement
    static class Config {
        @Bean OrderManagement orders(ApplicationEventPublisher events) { return new OrderManagement(events); }
        @Bean InventoryManagement inventory() { return new InventoryManagement(); }
        @Bean PlatformTransactionManager transactionManager() { return new RecordingManager(); }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            context.getBean(OrderManagement.class).complete(7);
        }
    }
}
