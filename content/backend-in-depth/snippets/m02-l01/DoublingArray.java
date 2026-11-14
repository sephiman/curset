public class DoublingArray {
    public static void main(String[] args) {
        int n = 1_000_000;
        int[] backing = new int[1];
        int size = 0;
        long copies = 0;
        for (int value = 0; value < n; value++) {
            if (size == backing.length) {
                int[] bigger = new int[backing.length * 2];
                for (int i = 0; i < size; i++) {
                    bigger[i] = backing[i];
                }
                copies += size;
                backing = bigger;
            }
            backing[size++] = value;
        }
        System.out.println("adds " + n);
        System.out.println("element copies " + copies);
        System.out.println("copies below 2n " + (copies < 2L * n));
    }
}
