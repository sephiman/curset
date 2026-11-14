import java.util.LinkedHashMap;
import java.util.Map;

public class MapOrder {
    static class Lru<K, V> extends LinkedHashMap<K, V> {
        private final int limit;

        Lru(int limit) {
            super(16, 0.75f, true);
            this.limit = limit;
        }

        @Override
        protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
            return size() > limit;
        }
    }

    public static void main(String[] args) {
        Map<String, Integer> insertion = new LinkedHashMap<>();
        insertion.put("a", 1);
        insertion.put("b", 2);
        insertion.put("c", 3);
        insertion.put("a", 10);
        System.out.println(insertion.keySet());

        Map<String, Integer> access = new LinkedHashMap<>(16, 0.75f, true);
        access.put("a", 1);
        access.put("b", 2);
        access.put("c", 3);
        access.get("a");
        System.out.println(access.keySet());

        Lru<String, Integer> lru = new Lru<>(2);
        lru.put("a", 1);
        lru.put("b", 2);
        lru.get("a");
        lru.put("c", 3);
        System.out.println(lru.keySet());
    }
}
