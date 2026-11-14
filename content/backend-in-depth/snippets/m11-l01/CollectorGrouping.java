import static java.util.stream.Collectors.counting;
import static java.util.stream.Collectors.groupingBy;
import static java.util.stream.Collectors.partitioningBy;

import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.stream.Stream;

public class CollectorGrouping {
    public static void main(String[] args) {
        List<String> words = List.of("apple", "avocado", "banana", "blueberry", "cherry", "apple");

        Map<Character, Map<Integer, Long>> byLetterThenLength = words.stream().collect(
                groupingBy(w -> w.charAt(0), TreeMap::new,
                        groupingBy(String::length, TreeMap::new, counting())));
        System.out.println(byLetterThenLength);

        Map<Boolean, Long> longOrShort = words.stream().collect(partitioningBy(w -> w.length() > 6, counting()));
        System.out.println(longOrShort);

        Map<Boolean, Long> noWords = Stream.<String>empty().collect(partitioningBy(w -> true, counting()));
        System.out.println(noWords);
    }
}
