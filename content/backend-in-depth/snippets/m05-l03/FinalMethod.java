import org.aopalliance.intercept.MethodInterceptor;
import org.springframework.aop.framework.ProxyFactory;

public class FinalMethod {
    public static class Account {
        public String open() { return "open"; }
        public final String close() { return "close"; }
    }

    public static void main(String[] args) {
        ProxyFactory factory = new ProxyFactory(new Account());
        factory.setProxyTargetClass(true);
        factory.addAdvice((MethodInterceptor) invocation -> {
            System.out.println("advice before " + invocation.getMethod().getName());
            return invocation.proceed();
        });
        Account proxy = (Account) factory.getProxy();
        proxy.open();
        proxy.close();
        System.out.println("done");
    }
}
