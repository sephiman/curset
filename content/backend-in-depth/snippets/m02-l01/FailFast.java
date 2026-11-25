import java.util.ArrayList;
import java.util.ConcurrentModificationException;
import java.util.Iterator;
import java.util.List;

public class FailFast {
    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>(List.of(1, 2, 3, 4));
        for (Integer value : values) {
            values.set(0, 99);
        }
        System.out.println("after set during iteration " + values);

        try {
            for (Integer value : values) {
                if (value == 99) {
                    values.add(5);
                }
            }
        } catch (ConcurrentModificationException e) {
            System.out.println("add during iteration throws ConcurrentModificationException");
        }

        Iterator<Integer> iterator = values.iterator();
        while (iterator.hasNext()) {
            if (iterator.next() == 2) {
                iterator.remove();
            }
        }
        System.out.println("after iterator remove " + values);
    }
}
