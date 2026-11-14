import java.util.concurrent.TimeoutException;

public class CauseChain {
    static void repository() throws TimeoutException {
        throw new TimeoutException("pool timeout after 30000 ms");
    }

    static void service() {
        try {
            repository();
        } catch (TimeoutException e) {
            throw new IllegalStateException("could not load order 17", e);
        }
    }

    static void controller() {
        try {
            service();
        } catch (IllegalStateException e) {
            throw new RuntimeException("request failed", e);
        }
    }

    public static void main(String[] args) {
        try {
            controller();
        } catch (RuntimeException caught) {
            for (Throwable t = caught; t != null; t = t.getCause()) {
                System.out.println(t.getMessage() + " (thrown in " + t.getStackTrace()[0].getMethodName() + ")");
            }
        }
    }
}
