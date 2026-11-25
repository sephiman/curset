import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;

public class ScopeIdentity {
    static int created;

    static class Counter {
        final int number = ++created;
    }

    @Configuration
    static class Config {
        @Bean
        Counter shared() {
            return new Counter();
        }

        @Bean
        @Scope("prototype")
        Counter fresh() {
            return new Counter();
        }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            System.out.println("created after refresh: " + created);
            System.out.println("same singleton: " + (context.getBean("shared") == context.getBean("shared")));
            System.out.println("same prototype: " + (context.getBean("fresh") == context.getBean("fresh")));
            System.out.println("created after four lookups: " + created);
        }
    }
}
