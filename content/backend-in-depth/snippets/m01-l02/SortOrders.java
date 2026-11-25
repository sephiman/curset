import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class SortOrders {
    public static void main(String[] args) {
        List<String> words = new ArrayList<>(List.of("pear", "fig", "apple"));
        Collections.sort(words, Comparator.comparingInt(String::length));
        System.out.println(words);
        Collections.sort(words, null);
        System.out.println(words);
        Collections.sort(words, Comparator.<String>naturalOrder().reversed());
        System.out.println(words);
    }
}
