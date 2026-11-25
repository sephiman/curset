import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

public class LifecycleOrder {
    static class Resource implements InitializingBean, DisposableBean {
        Resource() { System.out.println("constructor"); }
        @Autowired void setName(String name) { System.out.println("injection"); }
        @Override public void afterPropertiesSet() { System.out.println("after properties set"); }
        void init() { System.out.println("custom init"); }
        @Override public void destroy() { System.out.println("disposable destroy"); }
        void release() { System.out.println("custom release"); }
    }
    static class Tracer implements BeanPostProcessor {
        @Override public Object postProcessBeforeInitialization(Object bean, String name) {
            if (bean instanceof Resource) System.out.println("post-processor before");
            return bean;
        }
        @Override public Object postProcessAfterInitialization(Object bean, String name) {
            if (bean instanceof Resource) System.out.println("post-processor after");
            return bean;
        }
    }
    @Configuration
    static class Config {
        @Bean static Tracer tracer() { return new Tracer(); }
        @Bean String name() { return "resource"; }
        @Bean(initMethod = "init", destroyMethod = "release") Resource resource() { return new Resource(); }
    }
    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            System.out.println("context ready");
        }
    }
}
