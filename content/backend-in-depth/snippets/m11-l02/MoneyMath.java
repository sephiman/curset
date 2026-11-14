import java.math.BigDecimal;
import java.math.RoundingMode;

public class MoneyMath {
    public static void main(String[] args) {
        System.out.println(0.1 + 0.2);
        System.out.println(new BigDecimal("0.1").add(new BigDecimal("0.2")));
        System.out.println(new BigDecimal("1.10").multiply(new BigDecimal("2.0")));
        try {
            BigDecimal.ONE.divide(new BigDecimal("3"));
        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
        }
        BigDecimal share = new BigDecimal("100.00").divide(new BigDecimal("3"), 2, RoundingMode.HALF_UP);
        System.out.println(share);
        System.out.println(share.multiply(new BigDecimal("3")));
    }
}
