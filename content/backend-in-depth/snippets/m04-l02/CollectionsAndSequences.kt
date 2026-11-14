fun main() {
    val mutable = mutableListOf(1, 2)
    val readOnly: List<Int> = mutable
    mutable.add(3)
    println(readOnly)

    val words = listOf("The", "quick", "brown", "fox", "jumps")
    val log = mutableListOf<String>()
    val fromList = words
        .filter { log += "f:$it"; it.length > 3 }
        .map { log += "m:$it"; it.length }
        .take(2)
    println(log.joinToString(" "))

    log.clear()
    val pipeline = words.asSequence()
        .filter { log += "f:$it"; it.length > 3 }
        .map { log += "m:$it"; it.length }
        .take(2)
    println(log.isEmpty())
    val fromSequence = pipeline.toList()
    println(log.joinToString(" "))
    println(fromList == fromSequence)
}
