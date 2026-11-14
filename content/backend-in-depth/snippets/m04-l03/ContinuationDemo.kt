import kotlin.coroutines.Continuation
import kotlin.coroutines.EmptyCoroutineContext
import kotlin.coroutines.resume
import kotlin.coroutines.startCoroutine
import kotlin.coroutines.suspendCoroutine

var saved: Continuation<String>? = null

suspend fun awaitName(): String = suspendCoroutine { continuation -> saved = continuation }

suspend fun greet(): String {
    println("before suspension")
    val name = awaitName()
    println("after suspension")
    return "hello $name"
}

fun main() {
    val completion = Continuation<String>(EmptyCoroutineContext) { result ->
        println("result: ${result.getOrNull()}")
    }
    ::greet.startCoroutine(completion)
    println("main continues")
    saved?.resume("Kotlin")
    val generated = Class.forName("ContinuationDemoKt").declaredMethods.first { it.name == "greet" }
    println(generated.parameterTypes.map { it.simpleName })
    println(generated.returnType.simpleName)
}
