import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

public class ProfileSelection {
    @Configuration
    static class Config {
        @Bean @Profile("default") String store() { return "embedded"; }
        @Bean @Profile("cloud") String managedStore() { return "managed"; }
    }

    static void run(String... profiles) {
        try (var context = new AnnotationConfigApplicationContext()) {
            context.getEnvironment().setActiveProfiles(profiles);
            context.register(Config.class);
            context.refresh();
            System.out.println(profiles.length + " active profiles -> " + context.getBeansOfType(String.class).values());
        }
    }

    public static void main(String[] args) {
        run();
        run("cloud");
    }
}
