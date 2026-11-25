import java.util.Set;

public class TextSegmentation {
    static final Set<String> WORDS = Set.of("a", "aa", "aaa");
    static int wordTests;

    static boolean isWord(String text, int i, int j) {
        wordTests++;
        return WORDS.contains(text.substring(i, j));
    }

    static boolean backtracking(String text, int i) {
        if (i == text.length()) {
            return true;
        }
        for (int j = i + 1; j <= text.length(); j++) {
            if (isWord(text, i, j) && backtracking(text, j)) {
                return true;
            }
        }
        return false;
    }

    static boolean tabulated(String text) {
        int n = text.length();
        boolean[] splittable = new boolean[n + 1];
        splittable[n] = true;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j <= n; j++) {
                if (isWord(text, i, j) && splittable[j]) {
                    splittable[i] = true;
                }
            }
        }
        return splittable[0];
    }

    public static void main(String[] args) {
        String text = "aaaaaaaaaaaab";
        System.out.println("backtracking " + backtracking(text, 0) + " after " + wordTests + " word tests");
        wordTests = 0;
        System.out.println("table " + tabulated(text) + " after " + wordTests + " word tests");
    }
}
