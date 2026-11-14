import java.util.ArrayList;
import java.util.ConcurrentModificationException;
import java.util.Iterator;
import java.util.List;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;

public class ConcurrentCollections {
    public static void main(String[] args) {
        List<Integer> plain = new ArrayList<>(List.of(1, 2, 3));
        try {
            for (Integer value : plain) {
                plain.add(value + 10);
            }
        } catch (ConcurrentModificationException e) {
            System.out.println("ArrayList: ConcurrentModificationException");
        }

        List<Integer> snapshotList = new CopyOnWriteArrayList<>(List.of(1, 2, 3));
        Iterator<Integer> snapshot = snapshotList.iterator();
        snapshotList.add(4);
        int seen = 0;
        while (snapshot.hasNext()) {
            snapshot.next();
            seen++;
        }
        System.out.println("CopyOnWriteArrayList: iterator saw " + seen + " of " + snapshotList.size());
        try {
            snapshotList.iterator().remove();
        } catch (UnsupportedOperationException e) {
            System.out.println("iterator remove: UnsupportedOperationException");
        }

        ConcurrentHashMap<String, Integer> counts = new ConcurrentHashMap<>();
        counts.merge("a", 1, Integer::sum);
        counts.merge("a", 1, Integer::sum);
        System.out.println("merge result " + counts);
        try {
            counts.put(null, 1);
        } catch (NullPointerException e) {
            System.out.println("ConcurrentHashMap null key: NullPointerException");
        }

        BlockingQueue<String> queue = new ArrayBlockingQueue<>(1);
        System.out.println(queue.offer("first") + " " + queue.offer("second") + " " + queue.remainingCapacity());
        try {
            queue.add("third");
        } catch (IllegalStateException e) {
            System.out.println("add on a full queue: IllegalStateException");
        }
        System.out.println(queue.poll() + " " + queue.poll());
        try {
            queue.offer(null);
        } catch (NullPointerException e) {
            System.out.println("offer null: NullPointerException");
        }
    }
}
