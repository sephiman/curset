import static java.util.stream.Collectors.counting;
import static java.util.stream.Collectors.summingInt;
import static java.util.stream.Collectors.teeing;
import static java.util.stream.Collectors.toMap;

import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.TreeSet;

public class CollectorMerging {
    public static void main(String[] args) {
        List<String> words = List.of("apple", "avocado", "banana", "blueberry", "cherry", "apple");

        Map<Character, Integer> lettersPerInitial = new TreeMap<>(words.stream().collect(
                toMap(w -> w.charAt(0), String::length, Integer::sum)));
        System.out.println(lettersPerInitial);

        String both = words.stream().collect(
                teeing(summingInt(String::length), counting(),
                        (letters, count) -> letters + " letters in " + count + " words"));
        System.out.println(both);

        try {
            words.stream().collect(toMap(w -> w, String::length));
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
        }

        TreeSet<Integer> lengths = words.stream().collect(
                TreeSet::new, (set, w) -> set.add(w.length()), TreeSet::addAll);
        System.out.println(lengths);
    }
}
