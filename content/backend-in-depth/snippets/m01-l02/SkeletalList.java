import java.util.AbstractList;
import java.util.List;

public class SkeletalList {
    static final class Squares extends AbstractList<Integer> {
        private final int size;

        Squares(int size) {
            this.size = size;
        }

        @Override
        public Integer get(int index) {
            return index * index;
        }

        @Override
        public int size() {
            return size;
        }
    }

    public static void main(String[] args) {
        List<Integer> squares = new Squares(5);
        StringBuilder seen = new StringBuilder();
        for (int square : squares) {
            seen.append(square).append(' ');
        }
        System.out.println(seen.toString().trim());
        try {
            squares.add(25);
        } catch (UnsupportedOperationException e) {
            System.out.println("add is not implemented");
        }
    }
}
