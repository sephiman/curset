import java.util.ArrayList;
import java.util.List;

public class NQueens {
    static int calls;

    static void place(int[] columns, int row, List<String> solutions) {
        calls++;
        if (row == columns.length) {
            solutions.add(java.util.Arrays.toString(columns));
            return;
        }
        for (int column = 0; column < columns.length; column++) {
            if (isLegal(columns, row, column)) {
                columns[row] = column;
                place(columns, row + 1, solutions);
            }
        }
    }

    static boolean isLegal(int[] columns, int row, int column) {
        for (int earlier = 0; earlier < row; earlier++) {
            int distance = row - earlier;
            if (columns[earlier] == column || columns[earlier] == column + distance || columns[earlier] == column - distance) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        List<String> solutions = new ArrayList<>();
        place(new int[4], 0, solutions);
        System.out.println("4 queens " + solutions);
        System.out.println("recursive calls " + calls);
    }
}
