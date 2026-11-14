import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.time.Duration;
import java.util.Optional;

public class Timeouts {
    static String shown(Optional<Duration> timeout) {
        return timeout.map(Duration::toString).orElse("none");
    }

    public static void main(String[] args) {
        URI uri = URI.create("http://localhost/");
        System.out.println(shown(HttpClient.newHttpClient().connectTimeout()));
        System.out.println(shown(HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(2)).build().connectTimeout()));
        System.out.println(shown(HttpRequest.newBuilder(uri).build().timeout()));
        System.out.println(shown(HttpRequest.newBuilder(uri).timeout(Duration.ofSeconds(1)).build().timeout()));
    }
}
