import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.LongUnaryOperator;

public class StrategyObserver {
    static final class Checkout {
        private final LongUnaryOperator discount;
        private final List<Consumer<Long>> listeners = new ArrayList<>();

        Checkout(LongUnaryOperator discount) {
            this.discount = discount;
        }

        void subscribe(Consumer<Long> listener) {
            listeners.add(listener);
        }

        long pay(long cents) {
            long total = discount.applyAsLong(cents);
            listeners.forEach(listener -> listener.accept(total));
            return total;
        }
    }

    public static void main(String[] args) {
        Checkout half = new Checkout(cents -> cents / 2);
        half.subscribe(total -> System.out.println("audit " + total));
        half.subscribe(total -> System.out.println("mail " + total));
        System.out.println(half.pay(1000));
        System.out.println(new Checkout(cents -> cents).pay(1000));
    }
}
