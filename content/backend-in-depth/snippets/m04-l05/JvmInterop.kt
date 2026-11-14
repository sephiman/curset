import java.io.IOException
import java.lang.reflect.Modifier

class Greeter {
    companion object {
        @JvmStatic fun callStatic() {}
        fun callNonStatic() {}
    }
}

class Circle @JvmOverloads constructor(centerX: Int, centerY: Int, radius: Double = 1.0)

class Files {
    @Throws(IOException::class)
    fun declared() {}

    fun undeclared() {}
}

fun names(methods: Array<java.lang.reflect.Method>): List<String> =
    methods.filter { !it.isSynthetic }.map { it.name }.sorted()

fun main() {
    val staticOnGreeter = Greeter::class.java.declaredMethods.filter { Modifier.isStatic(it.modifiers) }
    println("static methods of Greeter: " + names(staticOnGreeter.toTypedArray()))
    println("methods of Greeter.Companion: " + names(Greeter.Companion::class.java.declaredMethods))
    val arities = Circle::class.java.constructors.filter { !it.isSynthetic }.map { it.parameterCount }.sorted()
    println("Circle constructor parameter counts: $arities")
    println("declared throws: " + Files::class.java.getDeclaredMethod("declared").exceptionTypes.map { it.simpleName })
    println("undeclared throws: " + Files::class.java.getDeclaredMethod("undeclared").exceptionTypes.map { it.simpleName })
}
