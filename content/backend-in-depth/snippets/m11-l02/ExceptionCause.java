import java.io.IOException;

public class ExceptionCause {
    static void load() throws IOException {
        throw new IOException("disk full");
    }

    static void swallowsCause() {
        try {
            load();
        } catch (IOException e) {
            throw new IllegalStateException("load failed");
        }
    }

    static void keepsCause() {
        try {
            load();
        } catch (IOException e) {
            throw new IllegalStateException("load failed", e);
        }
    }

    static String describe(Throwable cause) {
        return cause == null ? "no cause" : cause.getMessage();
    }

    public static void main(String[] args) {
        try {
            swallowsCause();
        } catch (IllegalStateException e) {
            System.out.println("swallowed: " + describe(e.getCause()));
        }
        try {
            keepsCause();
        } catch (IllegalStateException e) {
            System.out.println("kept: " + describe(e.getCause()));
        }
    }
}
