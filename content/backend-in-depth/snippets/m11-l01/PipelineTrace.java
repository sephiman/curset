import java.util.stream.Stream;

public class PipelineTrace {
    public static void main(String[] args) {
        System.out.println(Stream.of("a", "b", "c", "d")
                .peek(s -> System.out.println("peek " + s))
                .map(String::toUpperCase)
                .filter(s -> s.equals("B"))
                .findFirst());

        long counted = Stream.of(1, 2, 3)
                .peek(n -> System.out.println("counting " + n))
                .count();
        System.out.println(counted);

        System.out.println(Stream.iterate(1, n -> n * 2).takeWhile(n -> n < 100).toList());

        Stream<Integer> used = Stream.of(1, 2);
        used.toList();
        try {
            used.toList();
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
        }
    }
}
