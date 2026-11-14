public class PropertyCounterexamples {
    public static void main(String[] args) {
        int smallest = Integer.MIN_VALUE;
        System.out.println("abs of smallest int = " + Math.abs(smallest));
        System.out.println("abs of smallest int >= 0: " + (Math.abs(smallest) >= 0));
        System.out.println("abs of largest int >= 0: " + (Math.abs(Integer.MAX_VALUE) >= 0));
        String string1 = "";
        String string2 = "a";
        String concatenated = string1 + string2;
        System.out.println("length of concatenation: " + concatenated.length());
        System.out.println("longer than string1: " + (concatenated.length() > string1.length()));
        System.out.println("longer than string2: " + (concatenated.length() > string2.length()));
    }
}
