class PlainBook(val isbn: String, val title: String)

data class Book(val isbn: String, val title: String)

data class Order(var id: Long? = null, val customer: String)

fun main() {
    println(PlainBook("978", "Kotlin") == PlainBook("978", "Kotlin"))
    println(Book("978", "Kotlin") == Book("978", "Kotlin"))
    println(Book("978", "Kotlin").hashCode() == Book("978", "Kotlin").hashCode())
    println(Book("978", "Kotlin"))
    val orders = HashSet<Order>()
    val order = Order(customer = "ada")
    orders.add(order)
    println(orders.contains(order))
    order.id = 7
    println(orders.contains(order))
}
