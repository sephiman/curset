import java.util.Locale;

public class QuotaShare {
    public static void main(String[] args) {
        double perBrokerQuota = 10.0;
        int brokers = 3;
        int producerInstances = 4;

        double clusterCeiling = perBrokerQuota * brokers;
        System.out.println(String.format(Locale.ROOT, "per-broker quota MB/s: %.1f", perBrokerQuota));
        System.out.println(String.format(Locale.ROOT, "cluster-wide ceiling MB/s: %.1f", clusterCeiling));
        System.out.println(String.format(Locale.ROOT, "share per producer instance at the ceiling MB/s: %.1f", clusterCeiling / producerInstances));
        System.out.println(String.format(Locale.ROOT, "share per producer instance on one broker MB/s: %.1f", perBrokerQuota / producerInstances));
    }
}
