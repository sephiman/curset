public class MoneyRecord {
    record Money(int cents, String currency) {
        Money {
            if (cents < 0) {
                throw new IllegalArgumentException("negative amount: " + cents);
            }
        }
    }

    public static void main(String[] args) {
        Money first = new Money(500, "EUR");
        Money copy = new Money(first.cents(), first.currency());
        System.out.println(first.equals(copy));
        System.out.println(first == copy);
        System.out.println(first);
        try {
            new Money(-1, "EUR");
        } catch (IllegalArgumentException rejected) {
            System.out.println(rejected.getMessage());
        }
    }
}
