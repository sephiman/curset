import java.util.Locale;

public class IndexCapacity {
    public static void main(String[] args) {
        long entriesPerSecond = 1_000;
        long secondsPerDay = 8 * 3_600;
        long days = 20;
        long entryBytes = 16;
        long pageBytes = 4_000;

        long entries = entriesPerSecond * secondsPerDay * days;
        long bytes = entries * entryBytes;
        System.out.println("seconds per day: " + secondsPerDay);
        System.out.println("entries: " + entries);
        System.out.println("bytes: " + bytes);
        System.out.println(String.format(Locale.ROOT, "gigabytes: %.1f", bytes / 1e9));
        System.out.println("leaf pages: " + bytes / pageBytes);
    }
}
