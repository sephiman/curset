import java.util.Map;

public class PortsAndAdapters {
    interface RateSource {
        int percentFor(int amount);
    }

    static class Discounter {
        private final RateSource rates;

        Discounter(RateSource rates) {
            this.rates = rates;
        }

        int discount(int amount) {
            return amount * rates.percentFor(amount) / 100;
        }
    }

    public static void main(String[] args) {
        RateSource constantRate = amount -> 5;
        Map<Integer, Integer> table = Map.of(100, 5, 200, 5, 1000, 10);
        RateSource inMemoryTable = table::get;
        for (RateSource source : new RateSource[] {constantRate, inMemoryTable}) {
            Discounter application = new Discounter(source);
            System.out.println(application.discount(100) + " " + application.discount(200) + " " + application.discount(1000));
        }
    }
}
