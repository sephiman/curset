fun lengthOrZero(text: String?): Int = text?.length ?: 0

fun expensiveDefault(): Int {
    println("default evaluated")
    return -1
}

fun main() {
    val missing: String? = null
    val present: String? = "abc"
    println(missing?.length)
    println(lengthOrZero("Kotlin"))
    println(lengthOrZero(missing))
    println(present?.length ?: expensiveDefault())
    println(missing?.length ?: expensiveDefault())
}
