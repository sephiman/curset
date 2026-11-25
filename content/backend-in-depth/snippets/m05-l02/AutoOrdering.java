import java.net.URL;
import java.net.URLClassLoader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import org.springframework.boot.autoconfigure.AutoConfiguration;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;

public class AutoOrdering {
    @AutoConfiguration(after = Zeta.class)
    public static class Alpha {
        @Bean String alphaBean() { return "alpha"; }
    }

    @AutoConfiguration
    public static class Zeta {
        @Bean String zetaBean() { return "zeta"; }
    }

    public static void main(String[] args) throws Exception {
        Path root = Files.createTempDirectory("order");
        Path file = root.resolve("META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports");
        Files.createDirectories(file.getParent());
        Files.writeString(file, "AutoOrdering$Alpha\nAutoOrdering$Zeta\n");
        var loader = new URLClassLoader(new URL[] {root.toUri().toURL()}, AutoOrdering.class.getClassLoader());
        try (var context = new AnnotationConfigApplicationContext()) {
            context.setClassLoader(loader);
            context.register(EnableAuto.class);
            context.refresh();
            System.out.println(List.of(context.getBeanDefinitionNames()).stream().filter(n -> n.endsWith("Bean")).map(n -> n.replace("Bean", "")).toList());
        }
    }

    @EnableAutoConfiguration
    public static class EnableAuto {}
}
