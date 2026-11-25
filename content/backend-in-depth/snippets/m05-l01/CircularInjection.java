import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

public class CircularInjection {
    static class A { B b; A() {} A(B b) { this.b = b; } @Autowired void setB(B b) { this.b = b; } }
    static class B { A a; B() {} B(A a) { this.a = a; } @Autowired void setA(A a) { this.a = a; } }

    @Configuration
    static class ByConstructor {
        @Bean A a(B b) { return new A(b); }
        @Bean B b(A a) { return new B(a); }
    }

    @Configuration
    static class BySetter {
        @Bean A a() { return new A(); }
        @Bean B b() { return new B(); }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(ByConstructor.class)) {
            System.out.println("constructor injection started");
        } catch (RuntimeException failure) {
            Throwable root = failure;
            while (root.getCause() != null) root = root.getCause();
            System.out.println("constructor injection failed with " + root.getClass().getSimpleName());
        }
        try (var context = new AnnotationConfigApplicationContext(BySetter.class)) {
            var a = context.getBean(A.class);
            System.out.println("setter injection closes the cycle: " + (a.b.a == a));
        }
    }
}
