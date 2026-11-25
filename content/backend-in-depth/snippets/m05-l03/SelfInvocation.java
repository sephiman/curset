import org.aopalliance.intercept.MethodInterceptor;
import org.springframework.aop.framework.ProxyFactory;

public class SelfInvocation {
    public interface Pojo { void foo(); void bar(); }

    public static class SimplePojo implements Pojo {
        public void foo() { System.out.println("foo runs"); this.bar(); }
        public void bar() { System.out.println("bar runs"); }
    }

    public static void main(String[] args) {
        MethodInterceptor advice = invocation -> {
            System.out.println("advice before " + invocation.getMethod().getName());
            return invocation.proceed();
        };
        ProxyFactory factory = new ProxyFactory(new SimplePojo());
        factory.addAdvice(advice);
        Pojo proxy = (Pojo) factory.getProxy();

        System.out.println("-- foo() through the proxy");
        proxy.foo();
        System.out.println("-- bar() through the proxy");
        proxy.bar();
    }
}
