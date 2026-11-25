import org.springframework.aop.framework.ProxyFactory;
import org.springframework.aop.support.AopUtils;

public class ProxyTypes {
    public interface Greeter { String greet(); }

    public static class EnglishGreeter implements Greeter {
        public String greet() { return "hello"; }
    }

    public static class Plain {
        public String name() { return "plain"; }
    }

    private static String kind(Object proxy) {
        if (AopUtils.isJdkDynamicProxy(proxy)) return "JDK dynamic proxy";
        return AopUtils.isCglibProxy(proxy) ? "CGLIB proxy" : "not a proxy";
    }

    public static void main(String[] args) {
        Object withInterface = new ProxyFactory(new EnglishGreeter()).getProxy();
        Object withoutInterface = new ProxyFactory(new Plain()).getProxy();
        ProxyFactory forced = new ProxyFactory(new EnglishGreeter());
        forced.setProxyTargetClass(true);
        Object forcedProxy = forced.getProxy();

        System.out.println("interface target: " + kind(withInterface));
        System.out.println("no interface: " + kind(withoutInterface));
        System.out.println("forced class proxy: " + kind(forcedProxy));
        System.out.println("forced proxy extends the target class: " + (forcedProxy instanceof EnglishGreeter));
        System.out.println("interface proxy extends the target class: " + (withInterface instanceof EnglishGreeter));
    }
}
