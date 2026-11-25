import java.net.URL;
import java.net.URLClassLoader;
import java.nio.file.Files;
import java.nio.file.Path;
import org.springframework.boot.autoconfigure.AutoConfiguration;
import org.springframework.boot.context.annotation.ImportCandidates;

public class ImportsFile {
    public static void main(String[] args) throws Exception {
        Path root = Files.createTempDirectory("imports");
        Path file = root.resolve("META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports");
        Files.createDirectories(file.getParent());
        Files.writeString(file, "# first\ncom.acme.FirstAutoConfiguration\ncom.acme.Outer$InnerAutoConfiguration\n");
        try (var loader = new URLClassLoader(new URL[] {root.toUri().toURL()}, null)) {
            var candidates = ImportCandidates.load(AutoConfiguration.class, loader).getCandidates();
            System.out.println(candidates.size() + " candidates");
            System.out.println("comment listed: " + candidates.contains("# first"));
            System.out.println("nested name kept: " + candidates.contains("com.acme.Outer$InnerAutoConfiguration"));
        }
    }
}
