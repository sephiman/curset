import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ListViews {
    public static void main(String[] args) {
        List<String> source = new ArrayList<>(List.of("tea"));
        List<String> view = Collections.unmodifiableList(source);
        List<String> copy = List.copyOf(source);
        source.add("milk");
        System.out.println(view);
        System.out.println(copy);
        try {
            view.add("rum");
        } catch (UnsupportedOperationException e) {
            System.out.println("view refuses add");
        }
        try {
            copy.add("rum");
        } catch (UnsupportedOperationException e) {
            System.out.println("copy refuses add");
        }
    }
}
