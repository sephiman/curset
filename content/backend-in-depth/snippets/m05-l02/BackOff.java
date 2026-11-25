import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

public class BackOff {
    record Greeter(String origin) {}

    @Configuration
    static class UserConfig {
        @Bean Greeter userGreeter() { return new Greeter("user"); }
    }

    @Configuration
    static class DefaultConfig {
        @Bean @ConditionalOnMissingBean Greeter defaultGreeter() { return new Greeter("default"); }
    }

    static void run(Class<?>... configurations) {
        try (var context = new AnnotationConfigApplicationContext(configurations)) {
            System.out.println(context.getBeansOfType(Greeter.class).values().stream().map(Greeter::origin).toList());
        }
    }

    public static void main(String[] args) {
        run(DefaultConfig.class);
        run(UserConfig.class, DefaultConfig.class);
    }
}
