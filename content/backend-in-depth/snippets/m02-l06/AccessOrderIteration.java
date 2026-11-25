import java.util.ConcurrentModificationException;
import java.util.LinkedHashMap;
import java.util.Map;

public class AccessOrderIteration {
    static String words(Exception e) {
        return e.getClass().getSimpleName().replace("Exception", "").replaceAll("([a-z])([A-Z])", "$1 $2").toLowerCase();
    }

    static String walkAndGet(boolean accessOrder) {
        Map<String, Integer> map = new LinkedHashMap<>(16, 0.75f, accessOrder);
        map.put("a", 1);
        map.put("b", 2);
        map.put("c", 3);
        StringBuilder visited = new StringBuilder();
        try {
            for (String key : map.keySet()) {
                visited.append(key);
                map.get(key);
            }
            return "visited " + visited;
        } catch (ConcurrentModificationException e) {
            return "visited " + visited + " then " + words(e);
        }
    }

    public static void main(String[] args) {
        System.out.println("access-ordered: " + walkAndGet(true));
        System.out.println("insertion-ordered: " + walkAndGet(false));
    }
}
