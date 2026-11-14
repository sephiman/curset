public class MemoryAreaErrors {
    static int depth = 0;

    static void recurse() {
        depth++;
        recurse();
    }

    public static void main(String[] args) {
        try {
            recurse();
        } catch (StackOverflowError e) {
            System.out.println("StackOverflowError after recursing: " + (depth > 1000));
        }
        try {
            int[] tooLarge = new int[Integer.MAX_VALUE];
            System.out.println(tooLarge.length);
        } catch (OutOfMemoryError e) {
            System.out.println("OutOfMemoryError: " + e.getMessage());
        }
    }
}
