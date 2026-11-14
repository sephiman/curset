import java.util.List;
import java.util.stream.Gatherers;
import java.util.stream.Stream;

public class GathererSteps {
    public static void main(String[] args) {
        System.out.println(Stream.of(1, 2, 3, 4, 5, 6, 7, 8).gather(Gatherers.windowFixed(3)).toList());
        System.out.println(Stream.of(1, 2, 3, 4, 5).gather(Gatherers.windowSliding(3)).toList());
        System.out.println(Stream.of(1, 2, 3, 4).gather(Gatherers.windowSliding(6)).toList());
        System.out.println(Stream.<Integer>empty().gather(Gatherers.windowFixed(3)).toList());
        System.out.println(Stream.of(1, 2, 3, 4, 5).gather(Gatherers.fold(() -> 0, Integer::sum)).toList());
        System.out.println(Stream.of(1, 2, 3, 4, 5).gather(Gatherers.scan(() -> 0, Integer::sum)).toList());
        List<List<Integer>> windows = Stream.of(1, 2, 3).gather(Gatherers.windowFixed(2)).toList();
        try {
            windows.get(0).add(9);
        } catch (UnsupportedOperationException e) {
            System.out.println("windows are unmodifiable");
        }
    }
}
