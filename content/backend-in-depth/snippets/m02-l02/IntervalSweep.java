import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.TreeSet;

public class IntervalSweep {
    record Event(int position, boolean left, int interval) {
    }

    public static void main(String[] args) {
        int[][] intervals = {{1, 4}, {2, 6}, {8, 10}, {5, 9}, {12, 13}};
        List<Event> events = new ArrayList<>();
        for (int i = 0; i < intervals.length; i++) {
            events.add(new Event(intervals[i][0], true, i));
            events.add(new Event(intervals[i][1], false, i));
        }
        events.sort(Comparator.comparingInt(Event::position).thenComparing(event -> !event.left()));

        TreeSet<Integer> active = new TreeSet<>();
        int mostOpen = 0;
        for (Event event : events) {
            if (event.left()) {
                active.forEach(other -> System.out.println("interval " + other + " overlaps " + event.interval()));
                active.add(event.interval());
                mostOpen = Math.max(mostOpen, active.size());
            } else {
                active.remove(event.interval());
            }
        }
        System.out.println("most intervals open at once " + mostOpen);
    }
}
