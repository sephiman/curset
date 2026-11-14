import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Duration;
import jdk.jfr.Event;
import jdk.jfr.Name;
import jdk.jfr.Recording;
import jdk.jfr.consumer.RecordingFile;

public class JfrEvents {
    @Name("demo.Order")
    static class OrderEvent extends Event {
        int orderId;
    }

    static long countRecorded(Duration threshold) throws Exception {
        Path file = Files.createTempFile("orders", ".jfr");
        try (Recording recording = new Recording()) {
            recording.enable("demo.Order").withThreshold(threshold);
            recording.start();
            for (int id = 1; id <= 3; id++) {
                OrderEvent event = new OrderEvent();
                event.begin();
                event.orderId = id;
                event.commit();
            }
            recording.stop();
            recording.dump(file);
        }
        long count = RecordingFile.readAllEvents(file).stream()
            .filter(event -> event.getEventType().getName().equals("demo.Order"))
            .count();
        Files.delete(file);
        return count;
    }

    public static void main(String[] args) throws Exception {
        System.out.println("threshold 0 ns: " + countRecorded(Duration.ZERO) + " events");
        System.out.println("threshold 1 h: " + countRecorded(Duration.ofHours(1)) + " events");
    }
}
