public class TabulatedPatterns {
    static int knapsack(int[] weights, int[] values, int capacity) {
        int[] best = new int[capacity + 1];
        for (int item = 0; item < weights.length; item++) {
            for (int c = capacity; c >= weights[item]; c--) {
                best[c] = Math.max(best[c], best[c - weights[item]] + values[item]);
            }
        }
        return best[capacity];
    }

    static int longestIncreasingSubsequence(int[] a) {
        int[] lisFirst = new int[a.length];
        int best = 0;
        for (int i = a.length - 1; i >= 0; i--) {
            lisFirst[i] = 1;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] > a[i]) {
                    lisFirst[i] = Math.max(lisFirst[i], 1 + lisFirst[j]);
                }
            }
            best = Math.max(best, lisFirst[i]);
        }
        return best;
    }

    static int editDistance(String from, String to) {
        int[][] edit = new int[from.length() + 1][to.length() + 1];
        for (int i = 0; i <= from.length(); i++) {
            edit[i][0] = i;
        }
        for (int j = 0; j <= to.length(); j++) {
            edit[0][j] = j;
        }
        for (int i = 1; i <= from.length(); i++) {
            for (int j = 1; j <= to.length(); j++) {
                int substitution = edit[i - 1][j - 1] + (from.charAt(i - 1) == to.charAt(j - 1) ? 0 : 1);
                edit[i][j] = Math.min(substitution, Math.min(edit[i - 1][j] + 1, edit[i][j - 1] + 1));
            }
        }
        return edit[from.length()][to.length()];
    }

    static long gridPaths(int rows, int columns) {
        long[][] paths = new long[rows][columns];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                paths[r][c] = r == 0 || c == 0 ? 1 : paths[r - 1][c] + paths[r][c - 1];
            }
        }
        return paths[rows - 1][columns - 1];
    }

    public static void main(String[] args) {
        System.out.println("knapsack " + knapsack(new int[] {1, 3, 4, 5}, new int[] {1, 4, 5, 7}, 7));
        System.out.println("longest increasing subsequence " + longestIncreasingSubsequence(new int[] {3, 1, 4, 1, 5, 9, 2, 6}));
        System.out.println("edit distance " + editDistance("FOOD", "MONEY"));
        System.out.println("grid paths " + gridPaths(3, 3));
    }
}
