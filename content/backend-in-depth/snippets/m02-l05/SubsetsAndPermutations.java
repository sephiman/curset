import java.util.ArrayList;
import java.util.List;

public class SubsetsAndPermutations {
    static void subsets(int[] items, int from, List<Integer> chosen, List<List<Integer>> out) {
        out.add(new ArrayList<>(chosen));
        for (int i = from; i < items.length; i++) {
            chosen.add(items[i]);
            subsets(items, i + 1, chosen, out);
            chosen.remove(chosen.size() - 1);
        }
    }

    static void permutations(int[] items, boolean[] used, List<Integer> chosen, List<List<Integer>> out) {
        if (chosen.size() == items.length) {
            out.add(new ArrayList<>(chosen));
            return;
        }
        for (int i = 0; i < items.length; i++) {
            if (!used[i]) {
                used[i] = true;
                chosen.add(items[i]);
                permutations(items, used, chosen, out);
                chosen.remove(chosen.size() - 1);
                used[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        int[] items = {1, 2, 3};
        List<List<Integer>> subsets = new ArrayList<>();
        subsets(items, 0, new ArrayList<>(), subsets);
        System.out.println("subsets " + subsets);

        List<List<Integer>> permutations = new ArrayList<>();
        permutations(items, new boolean[items.length], new ArrayList<>(), permutations);
        System.out.println("permutations " + permutations.size() + " first " + permutations.get(0)
                + " last " + permutations.get(permutations.size() - 1));
    }
}
