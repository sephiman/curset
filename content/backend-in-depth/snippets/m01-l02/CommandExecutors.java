import java.util.concurrent.Executor;

public class CommandExecutors {
    public static void main(String[] args) throws InterruptedException {
        Runnable command = () -> System.out.println(Thread.currentThread().getName());
        Executor direct = Runnable::run;
        direct.execute(command);
        Executor threadPerTask = task -> {
            Thread worker = new Thread(task, "worker");
            worker.start();
            try {
                worker.join();
            } catch (InterruptedException e) {
                throw new IllegalStateException(e);
            }
        };
        threadPerTask.execute(command);
    }
}
