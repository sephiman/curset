import java.util.concurrent.CompletableFuture;

public class CompletionComposition {
    public static void main(String[] args) {
        CompletableFuture<Integer> quantity = CompletableFuture.completedFuture(4);
        CompletableFuture<Integer> price = CompletableFuture.completedFuture(25);

        System.out.println(quantity.thenApply(units -> units * 10).join());
        System.out.println(quantity.thenCompose(units -> CompletableFuture.supplyAsync(() -> units + 1)).join());
        System.out.println(quantity.thenCombine(price, (units, each) -> units * each).join());

        CompletableFuture<Integer> failed = new CompletableFuture<>();
        failed.completeExceptionally(new IllegalStateException("price missing"));
        CompletableFuture<Integer> dependent = failed.thenApply(units -> units * 10);

        System.out.println("failed stage sees: " + failed.handle((value, error) -> error.getClass().getSimpleName()).join());
        System.out.println("dependent stage sees: " + dependent.handle((value, error) -> error.getClass().getSimpleName()).join());
        System.out.println("dependent cause: " + dependent.handle((value, error) -> error.getCause().getMessage()).join());
        System.out.println("exceptionally: " + dependent.exceptionally(error -> -1).join());
        System.out.println("handle on success: " + quantity.handle((value, error) -> error == null ? "ok " + value : "failed").join());
    }
}
