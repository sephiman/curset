import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class HeapAndTrie {
    static class Trie {
        private final Map<Character, Trie> children = new HashMap<>();
        private int wordsBelow;

        void insert(String word) {
            Trie node = this;
            node.wordsBelow++;
            for (char c : word.toCharArray()) {
                node = node.children.computeIfAbsent(c, key -> new Trie());
                node.wordsBelow++;
            }
        }

        int countWithPrefix(String prefix) {
            Trie node = this;
            for (char c : prefix.toCharArray()) {
                node = node.children.get(c);
                if (node == null) {
                    return 0;
                }
            }
            return node.wordsBelow;
        }
    }

    public static void main(String[] args) {
        int k = 3;
        PriorityQueue<Integer> smallestOfTheLargest = new PriorityQueue<>();
        for (int value : new int[] {5, 1, 9, 3, 7, 8, 2}) {
            smallestOfTheLargest.offer(value);
            if (smallestOfTheLargest.size() > k) {
                smallestOfTheLargest.poll();
            }
        }
        System.out.println("kth largest " + smallestOfTheLargest.peek());
        List<Integer> topK = new ArrayList<>(smallestOfTheLargest);
        Collections.sort(topK);
        System.out.println("top 3 " + topK);

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        maxHeap.addAll(List.of(5, 1, 9, 3));
        System.out.println("max-heap head " + maxHeap.peek());

        int i = 4;
        System.out.println("children of 4: " + (2 * i + 1) + " and " + (2 * i + 2) + ", parent of 4: " + (i - 1) / 2);

        try {
            smallestOfTheLargest.offer(null);
        } catch (NullPointerException e) {
            System.out.println("null is rejected");
        }

        Trie trie = new Trie();
        for (String word : new String[] {"car", "card", "care", "cat", "dog"}) {
            trie.insert(word);
        }
        System.out.println("words with prefix car: " + trie.countWithPrefix("car"));
        System.out.println("words with prefix ca: " + trie.countWithPrefix("ca"));
        System.out.println("words with prefix x: " + trie.countWithPrefix("x"));
    }
}
