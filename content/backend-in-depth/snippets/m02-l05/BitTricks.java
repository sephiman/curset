import java.util.BitSet;

public class BitTricks {
    public static void main(String[] args) {
        System.out.println("lowest one-bit of 40: " + Integer.lowestOneBit(40));
        System.out.println("leading zeros of 40: " + Integer.numberOfLeadingZeros(40));
        System.out.println("floor of log base 2 of 40: " + (31 - Integer.numberOfLeadingZeros(40)));
        System.out.println("highest bit rotated left by one: " + Integer.rotateLeft(1 << 31, 1));
        System.out.println("floor division and floor modulus of -4 by 3: " + Math.floorDiv(-4, 3) + " " + Math.floorMod(-4, 3));

        BitSet bits = new BitSet();
        bits.set(1);
        bits.set(3);
        bits.set(5);
        StringBuilder indices = new StringBuilder();
        for (int i = bits.nextSetBit(0); i >= 0; i = bits.nextSetBit(i + 1)) {
            indices.append(i).append(' ');
        }
        System.out.println("set bits " + indices.toString().trim());
        bits.flip(3);
        System.out.println("cardinality after the flip " + bits.cardinality());
        System.out.println("next set bit from 6: " + bits.nextSetBit(6));
    }
}
