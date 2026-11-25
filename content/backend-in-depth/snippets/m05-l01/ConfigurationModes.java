import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

public class ConfigurationModes {
    static int engines;

    static class Engine { Engine() { engines++; } }
    static class Car { Car(Engine engine) {} }

    @Configuration
    static class Full {
        @Bean Engine engine() { return new Engine(); }
        @Bean Car car() { return new Car(engine()); }
    }

    @Configuration(proxyBeanMethods = false)
    static class Lite {
        @Bean Engine engine() { return new Engine(); }
        @Bean Car car() { return new Car(engine()); }
    }

    static void run(Class<?> configuration) {
        engines = 0;
        try (var context = new AnnotationConfigApplicationContext(configuration)) {
            boolean subclass = context.getBean(configuration).getClass() != configuration;
            System.out.println(configuration.getSimpleName() + ": engines=" + engines + ", subclassed=" + subclass);
        }
    }

    public static void main(String[] args) {
        run(Full.class);
        run(Lite.class);
    }
}
