import java.util.ArrayDeque;
import java.util.Queue;

public class GridSearch {
    static final int[][] MOVES = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public static void main(String[] args) {
        String[] grid = {
            "S.#.",
            ".##.",
            "...E"
        };
        int rows = grid.length;
        int columns = grid[0].length();
        int[][] steps = new int[rows][columns];
        for (int[] row : steps) {
            java.util.Arrays.fill(row, -1);
        }
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {0, 0});
        steps[0][0] = 0;
        int reachable = 0;
        while (!queue.isEmpty()) {
            int[] cell = queue.remove();
            reachable++;
            for (int[] move : MOVES) {
                int r = cell[0] + move[0];
                int c = cell[1] + move[1];
                boolean inside = r >= 0 && r < rows && c >= 0 && c < columns;
                if (inside && grid[r].charAt(c) != '#' && steps[r][c] < 0) {
                    steps[r][c] = steps[cell[0]][cell[1]] + 1;
                    queue.add(new int[] {r, c});
                }
            }
        }
        System.out.println("steps to E " + steps[2][3]);
        System.out.println("reachable cells " + reachable);
    }
}
