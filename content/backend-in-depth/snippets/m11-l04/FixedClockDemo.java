import java.time.Clock;
import java.time.Instant;
import java.time.LocalDate;
import java.time.ZoneId;

public class FixedClockDemo {
    record Invoice(LocalDate dueDate) {
        boolean isOverdue(Clock clock) {
            return LocalDate.now(clock).isAfter(dueDate);
        }
    }

    public static void main(String[] args) {
        Instant instant = Instant.parse("2026-03-31T23:30:00Z");
        Clock utc = Clock.fixed(instant, ZoneId.of("UTC"));
        Clock madrid = Clock.fixed(instant, ZoneId.of("Europe/Madrid"));
        Invoice invoice = new Invoice(LocalDate.of(2026, 3, 31));
        System.out.println(LocalDate.now(utc));
        System.out.println(LocalDate.now(madrid));
        System.out.println(invoice.isOverdue(utc));
        System.out.println(invoice.isOverdue(madrid));
        System.out.println(utc.instant().equals(madrid.instant()));
    }
}
