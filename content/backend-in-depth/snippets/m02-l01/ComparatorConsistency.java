import java.util.Set;
import java.util.TreeSet;

public class ComparatorConsistency {
    public static void main(String[] args) {
        Set<String> caseBlind = new TreeSet<>(String.CASE_INSENSITIVE_ORDER);
        System.out.println("add a: " + caseBlind.add("a"));
        System.out.println("add A: " + caseBlind.add("A"));
        System.out.println("size " + caseBlind.size());

        Set<String> neverEqual = new TreeSet<>((x, y) -> 1);
        System.out.println("add a: " + neverEqual.add("a"));
        System.out.println("add a again: " + neverEqual.add("a"));
        System.out.println("size " + neverEqual.size());
    }
}
