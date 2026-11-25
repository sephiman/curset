import java.util.Map;
import org.springframework.boot.context.properties.bind.Bindable;
import org.springframework.boot.context.properties.bind.Binder;
import org.springframework.boot.context.properties.source.ConfigurationPropertySources;
import org.springframework.boot.context.properties.source.MapConfigurationPropertySource;
import org.springframework.core.env.SystemEnvironmentPropertySource;

public class RelaxedBinding {
    public static class Person {
        private String firstName;
        public String getFirstName() { return firstName; }
        public void setFirstName(String firstName) { this.firstName = firstName; }
    }

    static void bind(String label, Binder binder) {
        var bound = binder.bind("my.main-project.person", Bindable.of(Person.class));
        System.out.println(label + " -> " + bound.map(Person::getFirstName).orElse("unbound"));
    }

    public static void main(String[] args) {
        var spellings = Map.of("kebab case", "first-name", "camel case", "firstName", "underscore", "first_name");
        for (var spelling : new java.util.TreeMap<>(spellings).entrySet()) {
            var source = new MapConfigurationPropertySource(Map.of("my.main-project.person." + spelling.getValue(), "Rod"));
            bind(spelling.getKey(), new Binder(source));
        }
        var env = new SystemEnvironmentPropertySource("systemEnvironment", Map.of("MY_MAINPROJECT_PERSON_FIRSTNAME", "Rod"));
        bind("environment variable", new Binder(ConfigurationPropertySources.from(env)));
    }
}
