import java.util.HashMap;
import java.util.Map;

public class StepCounts {
    static int steps;

    static int quadratic(String s) {
        for (int i = 0; i < s.length(); i++) {
            int occurrences = 0;
            for (int j = 0; j < s.length(); j++) {
                steps++;
                if (s.charAt(i) == s.charAt(j)) {
                    occurrences++;
                }
            }
            if (occurrences == 1) {
                return i;
            }
        }
        return -1;
    }

    static int linear(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        for (char c : s.toCharArray()) {
            steps++;
            counts.merge(c, 1, Integer::sum);
        }
        for (int i = 0; i < s.length(); i++) {
            steps++;
            if (counts.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        for (int n : new int[] {100, 200}) {
            steps = 0;
            quadratic("ab".repeat(n / 2));
            System.out.println("quadratic n=" + n + ": " + steps);
        }
        for (int n : new int[] {100, 200}) {
            steps = 0;
            linear("ab".repeat(n / 2));
            System.out.println("linear n=" + n + ": " + steps);
        }
    }
}
