import java.util.List;

public class MutationDemo {
    static boolean original(int age) {
        return age >= 18;
    }

    static boolean mutant(int age) {
        return age > 18;
    }

    static boolean survives(List<Integer> testAges) {
        for (int age : testAges) {
            if (original(age) != mutant(age)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("tests with ages 10 and 30: mutant survives = " + survives(List.of(10, 30)));
        System.out.println("tests with ages 10, 18 and 30: mutant survives = " + survives(List.of(10, 18, 30)));
        for (int i : new int[] {2, 1}) {
            System.out.println("i >= 1 and i > 1 agree for i = " + i + ": " + ((i >= 1) == (i > 1)));
        }
    }
}
