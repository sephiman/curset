import java.util.Locale;

public class CoordinatedOmission {
    public static void main(String[] args) {
        long intervalMs = 10;
        long goodSamples = 10_000;
        long pauseMs = 100_000;

        long rawSamples = goodSamples + 1;
        double rawPercentAtOneMs = 100.0 * goodSamples / rawSamples;
        System.out.println("raw samples=" + rawSamples);
        System.out.println(String.format(Locale.ROOT, "raw percent at or below 1 ms=%.2f", rawPercentAtOneMs));

        long addedSamples = 0;
        for (long value = pauseMs - intervalMs; value > intervalMs; value -= intervalMs) {
            addedSamples++;
        }
        long correctedSamples = rawSamples + addedSamples;
        double correctedPercentAtOneMs = 100.0 * goodSamples / correctedSamples;
        System.out.println("added samples=" + addedSamples);
        System.out.println("corrected samples=" + correctedSamples);
        System.out.println(String.format(Locale.ROOT, "corrected percent at or below 1 ms=%.2f", correctedPercentAtOneMs));
    }
}
