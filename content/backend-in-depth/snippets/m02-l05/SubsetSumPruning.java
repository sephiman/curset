import java.util.ArrayList;
import java.util.List;

public class SubsetSumPruning {
    static int calls;

    static void search(int[] items, int index, int remaining, boolean prune, List<Integer> chosen,
            List<List<Integer>> found) {
        calls++;
        if (remaining == 0) {
            found.add(new ArrayList<>(chosen));
            return;
        }
        if (index == items.length || (prune && remaining < 0)) {
            return;
        }
        chosen.add(items[index]);
        search(items, index + 1, remaining - items[index], prune, chosen, found);
        chosen.remove(chosen.size() - 1);
        search(items, index + 1, remaining, prune, chosen, found);
    }

    public static void main(String[] args) {
        int[] items = {1, 2, 3, 4, 5};

        calls = 0;
        List<List<Integer>> found = new ArrayList<>();
        search(items, 0, 5, true, new ArrayList<>(), found);
        System.out.println("subsets that sum to 5 " + found);
        System.out.println("calls with pruning " + calls);

        calls = 0;
        search(items, 0, 5, false, new ArrayList<>(), new ArrayList<>());
        System.out.println("calls without pruning " + calls);
    }
}
