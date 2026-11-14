import java.util.BitSet;

public class FloorModAndBitSet {
    public static void main(String[] args) {
        System.out.println("floor modulus of -4 and 3: " + Math.floorMod(-4, 3));
        System.out.println("remainder of -4 and 3: " + (-4 % 3));

        BitSet seen = new BitSet();
        seen.set(1);
        seen.set(3);
        seen.set(5);
        System.out.println("bit set length " + seen.length() + ", set bits " + seen.cardinality());
    }
}
