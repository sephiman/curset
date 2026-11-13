import java.util.ArrayList;
import java.util.List;

public class ShallowRecord {
    record Order(String id, List<String> lines) {}

    record SafeOrder(String id, List<String> lines) {
        SafeOrder {
            if (id.isBlank()) {
                throw new IllegalArgumentException("id is blank");
            }
            lines = List.copyOf(lines);
        }
    }

    public static void main(String[] args) {
        List<String> lines = new ArrayList<>(List.of("tea"));
        Order order = new Order("A1", lines);
        SafeOrder safe = new SafeOrder("A1", lines);
        lines.add("milk");
        System.out.println(order);
        System.out.println(safe);
        System.out.println(order.equals(new Order(order.id(), order.lines())));
        try {
            new SafeOrder(" ", List.of());
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
