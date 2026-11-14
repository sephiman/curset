public class BinaryCounter {
    public static void main(String[] args) {
        boolean[] bits = new boolean[64];
        int n = 1000;
        long totalFlips = 0;
        long mostFlipsInOneIncrement = 0;
        for (int step = 1; step <= n; step++) {
            long flips = 0;
            int i = 0;
            while (bits[i]) {
                bits[i] = false;
                flips++;
                i++;
            }
            bits[i] = true;
            flips++;
            totalFlips += flips;
            mostFlipsInOneIncrement = Math.max(mostFlipsInOneIncrement, flips);
        }
        System.out.println("total flips " + totalFlips);
        System.out.println("most flips in one increment " + mostFlipsInOneIncrement);
        System.out.println("2n minus ones " + (2L * n - Integer.bitCount(n)));
    }
}
