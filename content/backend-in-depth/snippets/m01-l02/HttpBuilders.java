import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.time.Duration;
import java.util.concurrent.Executors;

public class HttpBuilders {
    public static void main(String[] args) {
        HttpRequest request = HttpRequest.newBuilder(URI.create("https://example.com/orders"))
                .header("Accept", "application/json")
                .timeout(Duration.ofSeconds(5))
                .GET()
                .build();
        System.out.println(request.method() + " " + request.uri().getPath());
        System.out.println(request.headers().firstValue("Accept").orElse("none"));
        System.out.println(request.timeout().orElseThrow());
        try (HttpClient client = HttpClient.newHttpClient()) {
            System.out.println(client.followRedirects());
            System.out.println(client.version() == HttpClient.Version.HTTP_2);
        }
        try {
            HttpRequest.newBuilder(URI.create("ftp://example.com/file"));
        } catch (IllegalArgumentException e) {
            System.out.println("unsupported scheme");
        }
        try {
            Executors.newFixedThreadPool(0);
        } catch (IllegalArgumentException e) {
            System.out.println("zero threads refused");
        }
    }
}
