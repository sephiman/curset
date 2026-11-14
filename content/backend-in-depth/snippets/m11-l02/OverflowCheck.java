public class OverflowCheck {
    public static void main(String[] args) {
        int top = Integer.MAX_VALUE;
        System.out.println(top + 1);
        try {
            Math.addExact(top, 1);
        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
        }
        long wrong = 1_000_000 * 5_000;
        long right = 1_000_000L * 5_000;
        System.out.println(wrong);
        System.out.println(right);
    }
}
