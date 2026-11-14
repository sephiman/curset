import java.util.Comparator;
import java.util.List;
import java.util.stream.Stream;

public class ComposedComparators {
    record Person(String name, String city) {}

    public static void main(String[] args) {
        List<Person> people = List.of(
                new Person("Zed", "Lyon"),
                new Person("amy", "Lyon"),
                new Person("Cid", null),
                new Person("Dee", "Oslo"));

        Comparator<Person> nullsFirst = Comparator
                .comparing(Person::city, Comparator.nullsFirst(Comparator.naturalOrder()))
                .thenComparing(Person::name, String.CASE_INSENSITIVE_ORDER);
        Comparator<Person> nullsLast = Comparator
                .comparing(Person::city, Comparator.nullsLast(Comparator.<String>naturalOrder()))
                .thenComparing(Person::name);

        System.out.println(names(people.stream().sorted(nullsFirst)));
        System.out.println(names(people.stream().sorted(nullsLast)));
    }

    private static List<String> names(Stream<Person> sorted) {
        return sorted.map(Person::name).toList();
    }
}
