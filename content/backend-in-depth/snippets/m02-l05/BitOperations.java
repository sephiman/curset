public class BitOperations {
    public static void main(String[] args) {
        System.out.println("ones in 11: " + Integer.bitCount(11));
        System.out.println("highest one-bit of 100: " + Integer.highestOneBit(100));
        System.out.println("trailing zeros of 40: " + Integer.numberOfTrailingZeros(40));
        System.out.println("64 is a power of two: " + ((64 & (64 - 1)) == 0));
        System.out.println("48 is a power of two: " + ((48 & (48 - 1)) == 0));
    }
}
