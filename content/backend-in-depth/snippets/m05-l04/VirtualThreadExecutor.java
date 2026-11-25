import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Executor;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.task.TaskExecutionAutoConfiguration;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;

public class VirtualThreadExecutor {
    @Configuration @Import(TaskExecutionAutoConfiguration.class)
    static class Config { }

    static void show(String property) throws Exception {
        try (ConfigurableApplicationContext context = new SpringApplicationBuilder(Config.class)
                .web(WebApplicationType.NONE).bannerMode(org.springframework.boot.Banner.Mode.OFF)
                .properties("spring.threads.virtual.enabled=" + property, "logging.level.root=OFF").run()) {
            Executor executor = context.getBean("applicationTaskExecutor", Executor.class);
            CompletableFuture<Boolean> virtual = new CompletableFuture<>();
            executor.execute(() -> virtual.complete(Thread.currentThread().isVirtual()));
            System.out.println("virtual=" + property + ": " + executor.getClass().getSimpleName() + ", virtual thread " + virtual.get());
        }
    }

    public static void main(String[] args) throws Exception {
        show("true");
        show("false");
    }
}
