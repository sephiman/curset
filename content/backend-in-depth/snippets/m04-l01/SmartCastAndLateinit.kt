class Report {
    lateinit var body: String
}

fun describe(data: Any): String {
    if (data !is String) return "not text"
    return "text of ${data.length} characters"
}

fun main() {
    println(describe("Kotlin"))
    println(describe(404))
    try {
        println(Report().body)
    } catch (e: UninitializedPropertyAccessException) {
        println(e.message)
    }
}
