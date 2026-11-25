public class PeasantMultiplication {
    static int calls;

    static int multiply(int x, int y) {
        calls++;
        if (x == 0) {
            return 0;
        }
        int product = multiply(x / 2, y + y);
        return x % 2 == 1 ? product + y : product;
    }

    public static void main(String[] args) {
        System.out.println("13 x 25 = " + multiply(13, 25) + " in " + calls + " calls");
        calls = 0;
        System.out.println("0 x 25 = " + multiply(0, 25) + " in " + calls + " call");
    }
}
