import java.time.Clock;
import java.time.Duration;
import java.time.Instant;
import java.time.LocalDate;
import java.time.ZoneId;
import java.time.ZoneOffset;

public class FixedClock {
    static boolean expired(Instant issuedAt, Clock clock) {
        return issuedAt.plus(Duration.ofMinutes(15)).isBefore(clock.instant());
    }

    public static void main(String[] args) {
        Instant issuedAt = Instant.parse("2026-01-01T00:00:00Z");
        Clock atBoundary = Clock.fixed(Instant.parse("2026-01-01T00:15:00Z"), ZoneOffset.UTC);
        Clock aSecondLater = Clock.offset(atBoundary, Duration.ofSeconds(1));
        System.out.println(expired(issuedAt, atBoundary));
        System.out.println(expired(issuedAt, aSecondLater));

        Instant lateEvening = Instant.parse("2026-01-01T23:30:00Z");
        System.out.println(LocalDate.now(Clock.fixed(lateEvening, ZoneOffset.UTC)));
        System.out.println(LocalDate.now(Clock.fixed(lateEvening, ZoneId.of("Asia/Tokyo"))));
    }
}
