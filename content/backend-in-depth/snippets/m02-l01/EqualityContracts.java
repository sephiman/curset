import java.math.BigDecimal;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

public class EqualityContracts {
    static class EqualsOnly {
        final int id;

        EqualsOnly(int id) {
            this.id = id;
        }

        @Override
        public boolean equals(Object other) {
            return other instanceof EqualsOnly that && that.id == id;
        }
    }

    static class EqualsAndHash extends EqualsOnly {
        EqualsAndHash(int id) {
            super(id);
        }

        @Override
        public int hashCode() {
            return Objects.hash(id);
        }
    }

    public static void main(String[] args) {
        System.out.println("equals: " + new EqualsOnly(7).equals(new EqualsOnly(7)));
        Set<EqualsOnly> broken = new HashSet<>();
        broken.add(new EqualsOnly(7));
        System.out.println("contains, equals only: " + broken.contains(new EqualsOnly(7)));

        Set<EqualsAndHash> working = new HashSet<>();
        working.add(new EqualsAndHash(7));
        System.out.println("contains, equals and hash code: " + working.contains(new EqualsAndHash(7)));

        BigDecimal four = new BigDecimal("4.0");
        BigDecimal fourPointZeroZero = new BigDecimal("4.00");
        System.out.println("decimal equals: " + four.equals(fourPointZeroZero));
        System.out.println("decimal compare: " + four.compareTo(fourPointZeroZero));

        Set<BigDecimal> hashed = new HashSet<>(Set.of(four, fourPointZeroZero));
        Set<BigDecimal> sorted = new TreeSet<>(Set.of(four, fourPointZeroZero));
        System.out.println("hashed size: " + hashed.size());
        System.out.println("sorted size: " + sorted.size());
    }
}
