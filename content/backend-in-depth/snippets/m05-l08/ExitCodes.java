import org.springframework.boot.Banner;
import org.springframework.boot.ExitCodeGenerator;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.context.annotation.Configuration;

public class ExitCodes {
    @Configuration
    static class App {}

    static int exitCode(ExitCodeGenerator... generators) {
        SpringApplication application = new SpringApplication(App.class);
        application.setWebApplicationType(WebApplicationType.NONE);
        application.setBannerMode(Banner.Mode.OFF);
        application.setLogStartupInfo(false);
        return SpringApplication.exit(application.run(), generators);
    }

    public static void main(String[] args) {
        ExitCodeGenerator ok = () -> 0;
        ExitCodeGenerator three = () -> 3;
        ExitCodeGenerator five = () -> 5;
        System.out.println(exitCode(ok, three, five));
        System.out.println(exitCode(five, ok, three));
        System.out.println(exitCode(ok));
    }
}
