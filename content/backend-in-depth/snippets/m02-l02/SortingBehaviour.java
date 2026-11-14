import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class SortingBehaviour {
    record Order(String customer, int priority) {
    }

    public static void main(String[] args) {
        List<Order> orders = new ArrayList<>(List.of(
                new Order("ana", 2), new Order("bo", 1), new Order("cy", 2),
                new Order("di", 1), new Order("ed", 2)));
        orders.sort(Comparator.comparingInt(Order::priority));
        System.out.println("by priority " + orders.stream().map(Order::customer).toList());

        int[] numbers = {5, 3, 9, 1, 7};
        Arrays.sort(numbers);
        System.out.println("sorted ints " + Arrays.toString(numbers));

        Object[] mixed = {"text", 1};
        try {
            Arrays.sort(mixed);
        } catch (ClassCastException e) {
            System.out.println("mixed types cannot be sorted");
        }

        String[] words = {"pear", "fig", "apple", "kiwi"};
        Arrays.sort(words, Comparator.comparingInt(String::length));
        System.out.println("by length " + Arrays.toString(words));

        int[] counts = new int[4];
        for (int value : new int[] {3, 1, 3, 0, 1, 3}) {
            counts[value]++;
        }
        System.out.println("counts " + Arrays.toString(counts));
    }
}
