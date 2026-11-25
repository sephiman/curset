import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.Banner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.availability.AvailabilityChangeEvent;
import org.springframework.boot.context.event.SpringApplicationEvent;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.event.ContextRefreshedEvent;

public class StartupEvents {
    @Configuration
    static class App {
        @Bean
        ApplicationRunner runner() {
            return args -> System.out.println("runner called");
        }
    }

    public static void main(String[] args) {
        SpringApplication application = new SpringApplication(App.class);
        application.setWebApplicationType(WebApplicationType.NONE);
        application.setBannerMode(Banner.Mode.OFF);
        application.setLogStartupInfo(false);
        application.addListeners(event -> {
            if (event instanceof SpringApplicationEvent || event instanceof ContextRefreshedEvent) {
                System.out.println(event.getClass().getSimpleName());
            } else if (event instanceof AvailabilityChangeEvent<?> change) {
                System.out.println("AvailabilityChangeEvent " + change.getState());
            }
        });
        application.run(args).close();
    }
}
