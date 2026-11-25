import java.util.TreeMap;
import org.springframework.boot.autoconfigure.condition.ConditionEvaluationReport;
import org.springframework.boot.autoconfigure.condition.ConditionalOnClass;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

public class ConditionReport {
    record Greeter() {}

    @Configuration
    static class UserConfig {
        @Bean Greeter userGreeter() { return new Greeter(); }
    }

    @Configuration
    static class DefaultConfig {
        @Bean @ConditionalOnMissingBean Greeter defaultGreeter() { return new Greeter(); }
        @Bean @ConditionalOnClass(name = "com.acme.Missing") String missingClass() { return "never"; }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext()) {
            var report = ConditionEvaluationReport.get(context.getDefaultListableBeanFactory());
            context.register(UserConfig.class, DefaultConfig.class);
            context.refresh();
            new TreeMap<>(report.getConditionAndOutcomesBySource()).forEach(
                (source, outcomes) -> System.out.println(source + " fullMatch=" + outcomes.isFullMatch()));
        }
    }
}
