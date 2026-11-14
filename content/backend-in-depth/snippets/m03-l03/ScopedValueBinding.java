public class ScopedValueBinding {
    private static final ScopedValue<String> NAME = ScopedValue.newInstance();

    static void show(String label) {
        System.out.println(label + " bound=" + NAME.isBound() + (NAME.isBound() ? " value=" + NAME.get() : ""));
    }

    public static void main(String[] args) throws InterruptedException {
        show("before");
        ScopedValue.where(NAME, "duke").run(() -> {
            show("inside");
            ScopedValue.where(NAME, "nested").run(() -> show("rebound"));
            show("after-rebound");
        });
        show("after");
        Thread other = new Thread(() -> ScopedValue.where(NAME, "duke2").run(() -> show("other thread")));
        ScopedValue.where(NAME, "duke1").run(() -> {
            other.start();
            try { other.join(); } catch (InterruptedException e) { throw new RuntimeException(e); }
            show("main thread");
        });
    }
}
