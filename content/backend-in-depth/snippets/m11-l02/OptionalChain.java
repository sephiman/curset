import java.util.Optional;

public class OptionalChain {
    static int lookups = 0;

    static String loadDefault() {
        lookups++;
        return "default";
    }

    public static void main(String[] args) {
        Optional<String> present = Optional.of("cached");

        System.out.println(present.orElse(loadDefault()));
        System.out.println("lookups after orElse: " + lookups);
        System.out.println(present.orElseGet(OptionalChain::loadDefault));
        System.out.println("lookups after orElseGet: " + lookups);
        System.out.println(present.or(() -> Optional.of(loadDefault())).get());
        System.out.println("lookups after or: " + lookups);

        System.out.println(present.map(value -> (String) null).isPresent());
        System.out.println(present.flatMap(value -> Optional.of(value.length())).get());
        System.out.println(present.filter(value -> value.isEmpty()).isPresent());
    }
}
