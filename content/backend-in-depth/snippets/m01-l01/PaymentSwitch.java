public class PaymentSwitch {
    sealed interface Payment permits Card, Transfer, Voucher {}

    record Card(String last4, long cents) implements Payment {}

    record Transfer(String iban, long cents) implements Payment {}

    record Voucher(String code) implements Payment {}

    record Receipt(String customer, Payment payment) {}

    static String describe(Payment payment) {
        return switch (payment) {
            case Card(String last4, long cents) -> "card " + last4 + " for " + cents;
            case Transfer(String iban, long cents) -> "transfer from " + iban + " for " + cents;
            case Voucher(String code) -> "voucher " + code;
        };
    }

    static String describe(Receipt receipt) {
        return switch (receipt) {
            case Receipt(String customer, Card(var last4, var cents)) -> customer + " paid by card " + last4;
            case Receipt(String customer, Transfer transfer) -> customer + " paid by transfer from " + transfer.iban();
            case Receipt(String customer, Voucher voucher) -> customer + " paid by voucher " + voucher.code();
        };
    }

    public static void main(String[] args) {
        System.out.println(describe(new Card("4242", 1500)));
        System.out.println(describe(new Voucher("W-9")));
        System.out.println(describe(new Receipt("Ana", new Transfer("ES00", 900))));
        try {
            describe((Payment) null);
        } catch (NullPointerException e) {
            System.out.println("NullPointerException");
        }
    }
}
