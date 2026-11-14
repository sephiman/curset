public class BackoffSchedule {
    static long next(long wait, double multiplier, long max) {
        return Math.min(Math.round(wait * multiplier), max);
    }

    public static void main(String[] args) {
        long wait = 1_000;
        StringBuilder waits = new StringBuilder();
        for (int retry = 1; retry <= 6; retry++) {
            if (retry > 1) {
                waits.append(", ");
            }
            waits.append(wait);
            wait = next(wait, 2.0, 10_000);
        }
        System.out.println(waits);
        System.out.println(Math.round(10_000 * 0.8) + " to " + Math.round(10_000 * 1.2));
    }
}
