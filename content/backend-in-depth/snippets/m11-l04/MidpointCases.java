public class MidpointCases {
    static int midpoint(int low, int high) {
        return (low + high) / 2;
    }

    public static void main(String[] args) {
        int[][] cases = {{0, 10}, {4, 4}, {Integer.MAX_VALUE - 1, Integer.MAX_VALUE}};
        for (int[] c : cases) {
            long expected = ((long) c[0] + c[1]) / 2;
            System.out.println(c[0] + "," + c[1] + " -> " + midpoint(c[0], c[1]) + " expected " + expected);
        }
    }
}
