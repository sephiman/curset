import java.util.ArrayList;
import java.util.Collections;
import java.util.Enumeration;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.Executors;

public class Wrappers {
    @SuppressWarnings({"unchecked", "rawtypes"})
    public static void main(String[] args) throws Exception {
        List<String> backing = new ArrayList<>();
        List<String> synced = Collections.synchronizedList(backing);
        synced.add("a");
        System.out.println(backing);
        List<Integer> checked = Collections.checkedList(new ArrayList<>(), Integer.class);
        try {
            ((List) checked).add("text");
        } catch (ClassCastException e) {
            System.out.println("checked list refused a String");
        }
        Enumeration<String> legacy = Collections.enumeration(List.of("x", "y"));
        System.out.println(Collections.list(legacy));
        Callable<Object> task = Executors.callable(() -> System.out.println("ran"));
        System.out.println(task.call());
    }
}
