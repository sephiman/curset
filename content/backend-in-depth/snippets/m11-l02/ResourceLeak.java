public class ResourceLeak {
    static class Connection implements AutoCloseable {
        private final String name;

        Connection(String name) {
            this.name = name;
            System.out.println("open " + name);
        }

        void query() {
            throw new IllegalStateException("query failed on " + name);
        }

        @Override
        public void close() {
            System.out.println("close " + name);
            throw new IllegalArgumentException("close failed on " + name);
        }
    }

    public static void main(String[] args) {
        try {
            Connection leaked = new Connection("manual");
            leaked.query();
            leaked.close();
        } catch (IllegalStateException e) {
            System.out.println("manual: " + e.getMessage());
        }

        try (Connection pooled = new Connection("resource")) {
            pooled.query();
        } catch (IllegalStateException e) {
            System.out.println("resource: " + e.getMessage());
            System.out.println("suppressed: " + e.getSuppressed()[0].getMessage());
        }
    }
}
