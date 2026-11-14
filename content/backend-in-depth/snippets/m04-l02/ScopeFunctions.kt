class Config {
    var host = ""
    var port = 0
}

fun main() {
    println("kotlin".let { it.length })
    println("kotlin".run { length + 1 })
    val config = Config().apply {
        host = "localhost"
        port = 8080
    }
    println("${config.host}:${config.port}")
    println(mutableListOf("a").also { it.add("b") })
    println(with(config) { port + 1 })
    val missing: String? = null
    println(missing?.let { it.length })
}
