import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

public class CandidateSelection {
    interface Notifier { String name(); }

    record Named(String name) implements Notifier {}

    record Consumer(String label, Notifier notifier) {}

    @Configuration
    static class Config {
        @Bean @Primary Notifier email() { return new Named("email"); }
        @Bean Notifier sms() { return new Named("sms"); }
        @Bean Consumer byPrimary(Notifier notifier) { return new Consumer("byPrimary", notifier); }
        @Bean Consumer byQualifier(@Qualifier("sms") Notifier notifier) { return new Consumer("byQualifier", notifier); }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            context.getBeansOfType(Consumer.class).values().stream()
                .sorted(java.util.Comparator.comparing(Consumer::label))
                .forEach(c -> System.out.println(c.label() + " -> " + c.notifier().name()));
        }
    }
}
