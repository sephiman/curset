public class BoxedIdentity {
    public static void main(String[] args) {
        int small = 127;
        int large = 128;
        Integer cachedA = small;
        Integer cachedB = small;
        Integer freshA = large;
        Integer freshB = large;
        System.out.println("127 with ==: " + (cachedA == cachedB));
        System.out.println("128 with ==: " + (freshA == freshB));
        System.out.println("128 with equals: " + freshA.equals(freshB));
        System.out.println("128 valueOf with ==: " + (Integer.valueOf(large) == Integer.valueOf(large)));
    }
}
