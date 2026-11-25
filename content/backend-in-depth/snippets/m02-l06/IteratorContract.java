import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class IteratorContract {
    static String words(Exception e) {
        return e.getClass().getSimpleName().replace("Exception", "").replaceAll("([a-z])([A-Z])", "$1 $2").toLowerCase();
    }

    static String outcome(Runnable action) {
        try {
            action.run();
            return "no exception";
        } catch (RuntimeException e) {
            return words(e);
        }
    }

    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>(List.of(1, 2, 3));
        Iterator<Integer> iterator = values.iterator();
        System.out.println("remove before next: " + outcome(iterator::remove));
        iterator.next();
        System.out.println("remove after next: " + outcome(iterator::remove));
        System.out.println("remove twice: " + outcome(iterator::remove));
        System.out.println("values " + values);
        iterator.forEachRemaining(v -> { });
        System.out.println("next at the end: " + outcome(iterator::next));

        Iterator<Integer> withoutRemove = new Iterator<>() {
            public boolean hasNext() { return false; }
            public Integer next() { throw new NoSuchElementException(); }
        };
        System.out.println("default remove: " + outcome(withoutRemove::remove));
    }
}
