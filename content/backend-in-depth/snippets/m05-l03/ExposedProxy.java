import org.aopalliance.intercept.MethodInterceptor;
import org.springframework.aop.framework.AopContext;
import org.springframework.aop.framework.ProxyFactory;

public class ExposedProxy {
    public interface Pojo { void foo(); void bar(); }

    public static class SimplePojo implements Pojo {
        public void foo() { ((Pojo) AopContext.currentProxy()).bar(); }
        public void bar() { System.out.println("bar runs"); }
    }

    private static void call(boolean exposeProxy) {
        ProxyFactory factory = new ProxyFactory(new SimplePojo());
        factory.addAdvice((MethodInterceptor) invocation -> {
            System.out.println("advice before " + invocation.getMethod().getName());
            return invocation.proceed();
        });
        factory.setExposeProxy(exposeProxy);
        try {
            ((Pojo) factory.getProxy()).foo();
        } catch (IllegalStateException e) {
            System.out.println("proxy not exposed: illegal state");
        }
    }

    public static void main(String[] args) {
        call(true);
        call(false);
    }
}
