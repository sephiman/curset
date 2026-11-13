import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Modifier;
import java.lang.reflect.Proxy;
import java.util.ArrayList;
import java.util.List;

public class ProxyDispatch {
    interface Greeter {
        String greet(String name);
    }

    public static void main(String[] args) {
        Greeter target = name -> "hello " + name;
        List<String> calls = new ArrayList<>();
        InvocationHandler handler = (proxy, method, arguments) -> {
            calls.add(method.getDeclaringClass().getSimpleName() + "." + method.getName());
            if (method.getName().equals("toString")) {
                return "proxy";
            }
            return method.invoke(target, arguments);
        };
        Greeter greeter = (Greeter) Proxy.newProxyInstance(
                Greeter.class.getClassLoader(), new Class<?>[] {Greeter.class}, handler);
        System.out.println(greeter.greet("Ana"));
        System.out.println(greeter);
        System.out.println(calls);
        System.out.println(Proxy.isProxyClass(greeter.getClass()));
        System.out.println(Modifier.isFinal(greeter.getClass().getModifiers()));
        System.out.println(greeter.getClass().getSuperclass().getName());
    }
}
