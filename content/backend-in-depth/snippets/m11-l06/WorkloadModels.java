import java.util.ArrayList;
import java.util.List;

public class WorkloadModels {
    record Result(int started, int peakInFlight) {}

    static Result run(boolean open, int testSeconds, int responseSeconds) {
        List<Integer> endTimes = new ArrayList<>();
        int peak = 0;
        int vuFreeAt = 0;
        for (int second = 0; second < testSeconds; second++) {
            boolean start = open || vuFreeAt <= second;
            if (!start) {
                continue;
            }
            endTimes.add(second + responseSeconds);
            vuFreeAt = second + responseSeconds;
            int now = second;
            peak = Math.max(peak, (int) endTimes.stream().filter(end -> end > now).count());
        }
        return new Result(endTimes.size(), peak);
    }

    public static void main(String[] args) {
        for (int responseSeconds : new int[] {6, 12}) {
            Result closed = run(false, 60, responseSeconds);
            Result open = run(true, 60, responseSeconds);
            System.out.println("closed, " + responseSeconds + " s responses: " + closed.started() + " started, peak " + closed.peakInFlight() + " in flight");
            System.out.println("open, " + responseSeconds + " s responses: " + open.started() + " started, peak " + open.peakInFlight() + " in flight");
        }
    }
}
