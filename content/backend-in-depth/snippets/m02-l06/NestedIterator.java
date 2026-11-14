import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class NestedIterator implements Iterator<Integer> {
    private final Iterator<List<Integer>> outer;
    private Iterator<Integer> inner = List.<Integer>of().iterator();

    NestedIterator(List<List<Integer>> nested) {
        this.outer = nested.iterator();
    }

    @Override
    public boolean hasNext() {
        while (!inner.hasNext() && outer.hasNext()) {
            inner = outer.next().iterator();
        }
        return inner.hasNext();
    }

    @Override
    public Integer next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        return inner.next();
    }

    static List<Integer> drain(List<List<Integer>> nested) {
        List<Integer> values = new ArrayList<>();
        new NestedIterator(nested).forEachRemaining(values::add);
        return values;
    }

    public static void main(String[] args) {
        System.out.println("values " + drain(List.of(List.of(1, 2), List.of(), List.of(3), List.of())));
        System.out.println("values of two empty lists " + drain(List.of(List.of(), List.of())));
    }
}
