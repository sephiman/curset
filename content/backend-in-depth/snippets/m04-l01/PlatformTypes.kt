fun main() {
    val fromJava = System.getProperty("curset.missing.property")
    val nullable: String? = fromJava
    println(nullable)
    try {
        val notNull: String = fromJava
        println(notNull)
    } catch (e: NullPointerException) {
        println("null pointer on assignment")
    }
}
