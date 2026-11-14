import java.util.HashMap;
import java.util.Map;

public class EdgeCases {
    static int firstUnique(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        for (char c : s.toCharArray()) {
            counts.merge(c, 1, Integer::sum);
        }
        for (int i = 0; i < s.length(); i++) {
            if (counts.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println("empty: " + firstUnique(""));
        System.out.println("no unique: " + firstUnique("aabb"));
        System.out.println("swiss: " + firstUnique("swiss"));
        System.out.println("surrogate pair: " + firstUnique("😀😁"));
    }
}
