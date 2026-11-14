import java.util.Locale;

public class TrafficEstimate {
    public static void main(String[] args) {
        long dailyUsers = 10_000_000;
        long writesPerUserPerDay = 5;
        long readsPerWrite = 10;
        long peakFactor = 3;
        long recordBytes = 1_000;
        long secondsPerDay = 86_400;
        long replicas = 3;

        long writesPerDay = dailyUsers * writesPerUserPerDay;
        long readsPerDay = writesPerDay * readsPerWrite;
        System.out.println("writes per day: " + writesPerDay);
        System.out.println("average writes per second: " + writesPerDay / secondsPerDay);
        System.out.println("peak writes per second: " + writesPerDay * peakFactor / secondsPerDay);
        System.out.println("average reads per second: " + readsPerDay / secondsPerDay);
        System.out.println("peak reads per second: " + readsPerDay * peakFactor / secondsPerDay);
        double gigabytesPerDay = writesPerDay * recordBytes / 1e9;
        System.out.println(String.format(Locale.ROOT, "gigabytes per day: %.0f", gigabytesPerDay));
        System.out.println(String.format(Locale.ROOT, "terabytes per year: %.2f", gigabytesPerDay * 365 / 1000));
        System.out.println(String.format(Locale.ROOT, "terabytes per year with %d replicas: %.2f", replicas, gigabytesPerDay * 365 * replicas / 1000));
    }
}
