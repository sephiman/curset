import java.util.ArrayList;
import java.util.List;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.beans.factory.support.DefaultListableBeanFactory;
import org.springframework.beans.factory.support.RootBeanDefinition;
import org.springframework.context.support.GenericApplicationContext;

public class FactoryVsContext {
    static final List<String> seen = new ArrayList<>();

    static class Recorder implements BeanPostProcessor {
        @Override
        public Object postProcessBeforeInitialization(Object bean, String beanName) {
            seen.add(beanName);
            return bean;
        }
    }

    static class Widget {}

    public static void main(String[] args) {
        var factory = new DefaultListableBeanFactory();
        factory.registerBeanDefinition("recorder", new RootBeanDefinition(Recorder.class));
        factory.registerBeanDefinition("widget", new RootBeanDefinition(Widget.class));
        factory.getBean("widget");
        System.out.println("plain factory processed: " + seen);

        seen.clear();
        try (var context = new GenericApplicationContext()) {
            context.registerBeanDefinition("recorder", new RootBeanDefinition(Recorder.class));
            context.registerBeanDefinition("widget", new RootBeanDefinition(Widget.class));
            context.refresh();
            System.out.println("application context processed: " + seen);
        }
    }
}
