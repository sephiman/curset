import java.lang.reflect.Modifier

class Service {
    fun work() {}
}

open class OpenService {
    open fun work() {}
}

fun main() {
    println("Service is final: " + Modifier.isFinal(Service::class.java.modifiers))
    println("Service.work is final: " + Modifier.isFinal(Service::class.java.getDeclaredMethod("work").modifiers))
    println("OpenService is final: " + Modifier.isFinal(OpenService::class.java.modifiers))
    println("OpenService.work is final: " + Modifier.isFinal(OpenService::class.java.getDeclaredMethod("work").modifiers))
}
