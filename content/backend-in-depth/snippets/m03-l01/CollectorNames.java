import java.lang.management.GarbageCollectorMXBean;
import java.lang.management.ManagementFactory;
import java.util.List;

public class CollectorNames {
    public static void main(String[] args) throws Exception {
        if (args.length > 0) {
            List<GarbageCollectorMXBean> beans = ManagementFactory.getGarbageCollectorMXBeans();
            beans.stream().map(GarbageCollectorMXBean::getName).sorted().forEach(System.out::println);
            return;
        }
        String java = ProcessHandle.current().info().command().orElseThrow();
        for (String flag : List.of("-XX:+UseSerialGC", "-XX:+UseParallelGC", "-XX:+UseG1GC", "-XX:+UseZGC")) {
            Process child = new ProcessBuilder(java, flag, "CollectorNames.java", "child")
                    .redirectErrorStream(true)
                    .start();
            String output = new String(child.getInputStream().readAllBytes()).strip().replace("\n", ", ");
            child.waitFor();
            System.out.println(flag + " -> " + output);
        }
    }
}
