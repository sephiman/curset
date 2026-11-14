interface Base {
    fun print()
}

class BaseImpl(val x: Int) : Base {
    override fun print() {
        println(x)
    }
}

class Derived(b: Base) : Base by b

val lazyValue: String by lazy {
    println("computed!")
    "Hello"
}

fun main() {
    Derived(BaseImpl(10)).print()
    println(lazyValue)
    println(lazyValue)
}
