data class User(val name: String, val age: Int)

sealed interface Shape {
    data class Circle(val radius: Double) : Shape
    data class Square(val side: Double) : Shape
    data object Empty : Shape
}

fun label(shape: Shape): String = when (shape) {
    is Shape.Circle if shape.radius > 10 -> "large circle"
    is Shape.Circle -> "circle"
    is Shape.Square -> "square"
    Shape.Empty -> "empty"
}

fun main() {
    val user = User("John", 42)
    println(user)
    println(user == User("John", 42))
    println(user.copy(age = 43))
    println(Shape.Empty)
    println(label(Shape.Circle(11.0)))
    println(label(Shape.Circle(1.0)))
}
