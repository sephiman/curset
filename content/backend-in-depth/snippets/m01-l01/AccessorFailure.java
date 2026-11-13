public class AccessorFailure {
    record Gauge(int reading) {
        @Override
        public int reading() {
            throw new IllegalStateException("sensor offline");
        }
    }

    public static void main(String[] args) {
        Object value = new Gauge(7);
        try {
            if (value instanceof Gauge(int reading)) {
                System.out.println(reading);
            }
        } catch (MatchException e) {
            System.out.println("MatchException caused by " + e.getCause());
        }
        System.out.println(value instanceof Gauge);
    }
}
