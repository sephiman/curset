import org.springframework.aop.support.AopUtils;
import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.cache.concurrent.ConcurrentMapCacheManager;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

public class CacheProxy {
    static int loads;

    static class Prices {
        @Cacheable("prices")
        public int price(String sku) {
            loads++;
            return sku.length() * 100;
        }

        public int again(String sku) {
            return price(sku);
        }
    }

    @Configuration
    @EnableCaching
    static class Config {
        @Bean
        CacheManager cacheManager() {
            return new ConcurrentMapCacheManager("prices");
        }

        @Bean
        Prices prices() {
            return new Prices();
        }
    }

    public static void main(String[] args) {
        try (var context = new AnnotationConfigApplicationContext(Config.class)) {
            Prices prices = context.getBean(Prices.class);
            System.out.println(AopUtils.isCglibProxy(prices));
            prices.price("tea");
            prices.price("tea");
            System.out.println(loads);
            prices.again("tea");
            System.out.println(loads);
        }
    }
}
