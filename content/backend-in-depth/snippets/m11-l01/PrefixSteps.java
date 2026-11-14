import java.util.List;
import java.util.stream.Stream;

public class PrefixSteps {
    public static void main(String[] args) {
        List<List<Integer>> nested = List.of(List.of(1, 2), List.of(), List.of(3));
        System.out.println(nested.stream().flatMap(List::stream).toList());
        System.out.println(Stream.of(1, 2, 5, 1, 6).filter(n -> n < 3).toList());
        System.out.println(Stream.of(1, 2, 5, 1, 6).takeWhile(n -> n < 3).toList());
        System.out.println(Stream.of(1, 2, 5, 1, 6).dropWhile(n -> n < 3).toList());
        System.out.println(Stream.of(1, 2, 3, 4).reduce(10, Integer::sum));
    }
}
