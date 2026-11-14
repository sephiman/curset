import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;

public class ZoneTransitions {
    public static void main(String[] args) {
        ZoneId paris = ZoneId.of("Europe/Paris");

        System.out.println(ZonedDateTime.of(LocalDateTime.of(2026, 3, 29, 2, 30), paris));

        ZonedDateTime overlap = ZonedDateTime.of(LocalDateTime.of(2026, 10, 25, 2, 30), paris);
        System.out.println(overlap);
        System.out.println(overlap.withLaterOffsetAtOverlap());

        ZonedDateTime saturday = ZonedDateTime.of(LocalDateTime.of(2026, 3, 28, 12, 0), paris);
        System.out.println(saturday.plusDays(1));
        System.out.println(saturday.plusHours(24));
    }
}
