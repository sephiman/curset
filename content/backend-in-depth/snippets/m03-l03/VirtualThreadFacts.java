public class VirtualThreadFacts {
    public static void main(String[] args) throws InterruptedException {
        Thread virtual = Thread.ofVirtual().unstarted(() -> {});
        Thread platform = Thread.ofPlatform().unstarted(() -> {});
        System.out.println("virtual-thread virtual=" + virtual.isVirtual());
        System.out.println("virtual-thread name=[" + virtual.getName() + "]");
        System.out.println("virtual-thread daemon=" + virtual.isDaemon());
        System.out.println("platform-thread virtual=" + platform.isVirtual());
        System.out.println("platform-thread daemon=" + platform.isDaemon());
        Thread.ofVirtual().start(() ->
            System.out.println("current-thread inside virtual=" + Thread.currentThread().isVirtual())).join();
    }
}
