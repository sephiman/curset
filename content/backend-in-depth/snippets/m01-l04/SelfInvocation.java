import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;
import java.util.ArrayList;
import java.util.List;

public class SelfInvocation {
    interface Pojo {
        void foo();

        void bar();
    }

    static class SimplePojo implements Pojo {
        public void foo() {
            this.bar();
        }

        public void bar() {
        }
    }

    public static void main(String[] args) {
        Pojo target = new SimplePojo();
        List<String> intercepted = new ArrayList<>();
        InvocationHandler handler = (proxy, method, arguments) -> {
            intercepted.add(method.getName());
            return method.invoke(target, arguments);
        };
        Pojo pojo = (Pojo) Proxy.newProxyInstance(
                Pojo.class.getClassLoader(), new Class<?>[] {Pojo.class}, handler);

        pojo.foo();
        System.out.println(intercepted);
        intercepted.clear();
        pojo.bar();
        System.out.println(intercepted);
    }
}
