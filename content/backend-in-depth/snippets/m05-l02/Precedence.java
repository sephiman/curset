import java.util.Map;
import org.springframework.boot.Banner;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.annotation.Configuration;

public class Precedence {
    @Configuration
    static class Config {}

    static void run(String... args) {
        var context = new SpringApplicationBuilder(Config.class)
            .web(WebApplicationType.NONE)
            .bannerMode(Banner.Mode.OFF)
            .logStartupInfo(false)
            .properties(Map.of("acme.name", "default"))
            .run(args);
        System.out.println((args.length == 0 ? "no arguments" : "command line argument") + " -> " + context.getEnvironment().getProperty("acme.name"));
        context.close();
    }

    public static void main(String[] args) {
        run();
        System.setProperty("acme.name", "system");
        run();
        run("--acme.name=cli");
    }
}
