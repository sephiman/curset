public class MissingCase {
    sealed interface Payment permits Card, Transfer, Voucher {}

    record Card(String last4) implements Payment {}

    record Transfer(String iban) implements Payment {}

    record Voucher(String code) implements Payment {}

    static String describe(Payment payment) {
        return switch (payment) {
            case Card card -> "card " + card.last4();
            case Transfer transfer -> "transfer " + transfer.iban();
        };
    }

    public static void main(String[] args) {
        System.out.println(describe(new Voucher("W-9")));
    }
}
