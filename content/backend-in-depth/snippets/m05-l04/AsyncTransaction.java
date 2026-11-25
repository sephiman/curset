import java.util.concurrent.CompletableFuture;
import org.springframework.context.annotation.*;
import org.springframework.scheduling.annotation.*;
import org.springframework.transaction.*;
import org.springframework.transaction.annotation.*;
import org.springframework.transaction.support.*;

public class AsyncTransaction {
    static class RecordingManager extends AbstractPlatformTransactionManager {
        protected Object doGetTransaction() { return new Object(); }
        protected void doBegin(Object tx, TransactionDefinition d) { }
        protected void doCommit(DefaultTransactionStatus s) { }
        protected void doRollback(DefaultTransactionStatus s) { }
    }
    public static class Worker {
        @Async public CompletableFuture<Boolean> transactionActive() {
            return CompletableFuture.completedFuture(TransactionSynchronizationManager.isActualTransactionActive());
        }
    }
    @Configuration @EnableAsync @EnableTransactionManagement
    static class Config {
        @Bean Worker worker() { return new Worker(); }
        @Bean PlatformTransactionManager transactionManager() { return new RecordingManager(); }
    }
    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            Worker worker = context.getBean(Worker.class);
            new TransactionTemplate(context.getBean(PlatformTransactionManager.class)).executeWithoutResult(status -> {
                System.out.println("caller: " + TransactionSynchronizationManager.isActualTransactionActive());
                System.out.println("async method: " + worker.transactionActive().join());
            });
        }
    }
}
