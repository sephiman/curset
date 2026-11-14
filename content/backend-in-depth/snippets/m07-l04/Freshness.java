public class Freshness {
    static boolean responseIsFresh(long freshnessLifetime, long currentAge) {
        return freshnessLifetime > currentAge;
    }

    public static void main(String[] args) {
        for (long age : new long[] {59, 60, 61}) {
            String state = responseIsFresh(60, age) ? "fresh" : "stale";
            System.out.println("lifetime 60, age " + age + ": " + state);
        }
    }
}
