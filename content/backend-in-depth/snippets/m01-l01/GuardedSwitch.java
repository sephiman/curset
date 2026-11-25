public class GuardedSwitch {
    static String classify(Object value) {
        return switch (value) {
            case Integer i when i > 100 -> "big " + i;
            case Integer i -> "int " + i;
            case CharSequence text -> "text of " + text.length();
            case null, default -> "other";
        };
    }

    public static void main(String[] args) {
        System.out.println(classify(500));
        System.out.println(classify(7));
        System.out.println(classify("abc"));
        System.out.println(classify(new StringBuilder("hello")));
        System.out.println(classify(2.5));
        System.out.println(classify(null));
    }
}
