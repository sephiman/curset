import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class LruCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;

    LruCache(int capacity) {
        super(16, 0.75f, true);
        this.capacity = capacity;
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }

    public static void main(String[] args) {
        LruCache<String, Integer> cache = new LruCache<>(3);
        cache.put("a", 1);
        cache.put("b", 2);
        cache.put("c", 3);
        cache.get("a");
        cache.put("d", 4);
        System.out.println("access-ordered " + List.copyOf(cache.keySet()));

        Map<String, Integer> insertionOrdered = new LinkedHashMap<>();
        insertionOrdered.put("a", 1);
        insertionOrdered.put("b", 2);
        insertionOrdered.put("c", 3);
        insertionOrdered.put("a", 4);
        System.out.println("insertion-ordered " + List.copyOf(insertionOrdered.keySet()));
    }
}
