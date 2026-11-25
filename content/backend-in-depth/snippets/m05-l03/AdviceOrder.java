import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.core.annotation.Order;

public class AdviceOrder {
    public static class Service { public void work() { System.out.println("work"); } }

    public abstract static class Traced {
        @Around("execution(* AdviceOrder.Service.work(..))")
        public Object around(ProceedingJoinPoint pjp) throws Throwable {
            System.out.println(getClass().getSimpleName() + " in");
            Object result = pjp.proceed();
            System.out.println(getClass().getSimpleName() + " out");
            return result;
        }
    }

    @Aspect @Order(2) public static class Second extends Traced { }
    @Aspect @Order(1) public static class First extends Traced { }

    @Configuration @EnableAspectJAutoProxy
    static class Config {
        @Bean Service service() { return new Service(); }
        @Bean Second second() { return new Second(); }
        @Bean First first() { return new First(); }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            context.getBean(Service.class).work();
        }
    }
}
