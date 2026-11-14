interface Source<out T> {
    fun nextT(): T
}

fun widen(strings: Source<String>): Source<Any> = strings

inline fun <reified T> isInstance(value: Any): Boolean = value is T

fun main() {
    val strings = object : Source<String> {
        override fun nextT(): String = "kotlin"
    }
    println(widen(strings).nextT())
    println(isInstance<String>("kotlin"))
    println(isInstance<Int>("kotlin"))
    println(arrayListOf<String>()::class == arrayListOf<Int>()::class)
}
