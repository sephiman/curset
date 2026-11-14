import java.nio.file.Path;

public class PathTraversal {
    public static void main(String[] args) {
        Path uploads = Path.of("/var/uploads");
        Path requested = uploads.resolve("../etc/passwd").normalize();
        System.out.println(requested + " " + requested.startsWith(uploads));
    }
}
