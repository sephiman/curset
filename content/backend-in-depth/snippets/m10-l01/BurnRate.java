public class BurnRate {
    public static void main(String[] args) {
        long periodHours = 30 * 24;
        System.out.println("burn rate for 5% in 1 hour: " + 5 * periodHours / (100 * 1));
        System.out.println("budget consumed at 14.4 over 1 hour: " + 144 * 1 * 100 / (10 * periodHours) + "%");
        System.out.println("hours to exhaust at burn rate 10: " + periodHours / 10);
    }
}
