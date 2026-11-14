public class SizingArithmetic {
    public static void main(String[] args) {
        long retentionSeconds = 15 * 24 * 3_600;
        long samplesPerSecond = 100_000;
        long bytesPerSample = 2;
        System.out.println("retention seconds: " + retentionSeconds);
        System.out.println("needed bytes: " + retentionSeconds * samplesPerSecond * bytesPerSample);
        System.out.println("desired replicas for 4 pods at 200m against 100m: " + Math.ceilDiv(4 * 200, 100));
        System.out.println("desired replicas for 3 pods at 150m against 100m: " + Math.ceilDiv(3 * 150, 100));
        System.out.println("retention size cap for a 500 GB disk at 85%: " + 500 * 85 / 100);
    }
}
