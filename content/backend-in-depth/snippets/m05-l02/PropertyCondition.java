import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

public class PropertyCondition {
    @Configuration
    static class Config {
        @Bean @ConditionalOnProperty(prefix = "acme", name = "feature") String feature() { return "on"; }
    }

    static void run(String value) {
        try (var context = new AnnotationConfigApplicationContext()) {
            if (value != null) System.setProperty("acme.feature", value);
            context.register(Config.class);
            context.refresh();
            System.out.println(value + " -> " + (context.getBeansOfType(String.class).isEmpty() ? "off" : "on"));
        } finally {
            System.clearProperty("acme.feature");
        }
    }

    public static void main(String[] args) {
        run(null);
        run("false");
        run("true");
        run("0");
    }
}
