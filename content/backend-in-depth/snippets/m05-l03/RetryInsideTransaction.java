import java.util.concurrent.atomic.AtomicInteger;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.resilience.annotation.EnableResilientMethods;
import org.springframework.resilience.annotation.Retryable;
import org.springframework.transaction.*;
import org.springframework.transaction.annotation.*;
import org.springframework.transaction.support.*;

public class RetryInsideTransaction {
    static class RecordingManager extends AbstractPlatformTransactionManager {
        protected Object doGetTransaction() { return new Object(); }
        protected void doBegin(Object tx, TransactionDefinition d) { System.out.println("begin"); }
        protected void doCommit(DefaultTransactionStatus s) { System.out.println("commit"); }
        protected void doRollback(DefaultTransactionStatus s) { System.out.println("rollback"); }
    }

    public static class Payments {
        private final AtomicInteger attempts = new AtomicInteger();
        @Retryable(maxRetries = 2, delay = 0)
        @Transactional
        public void charge() {
            System.out.println("attempt " + attempts.incrementAndGet());
            if (attempts.get() < 3) throw new IllegalStateException("try again");
        }
    }
    @Configuration @EnableTransactionManagement @EnableResilientMethods
    static class Config {
        @Bean Payments payments() { return new Payments(); }
        @Bean PlatformTransactionManager transactionManager() { return new RecordingManager(); }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            context.getBean(Payments.class).charge();
        }
    }
}
