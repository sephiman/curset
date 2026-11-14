import java.time.Clock;
import java.time.Instant;
import java.time.ZoneOffset;

public class ExpiryBoundary {
    static boolean isExpired(Instant expiresAt, Clock clock) {
        return clock.instant().isAfter(expiresAt);
    }

    public static void main(String[] args) {
        Instant expiresAt = Instant.parse("2026-01-01T00:00:00Z");
        for (long offsetSeconds : new long[] {-1, 0, 1}) {
            Clock clock = Clock.fixed(expiresAt.plusSeconds(offsetSeconds), ZoneOffset.UTC);
            System.out.println("offset " + offsetSeconds + ": " + isExpired(expiresAt, clock));
        }
        Clock stopped = Clock.fixed(expiresAt, ZoneOffset.UTC);
        System.out.println("same instant twice: " + stopped.instant().equals(stopped.instant()));
    }
}
