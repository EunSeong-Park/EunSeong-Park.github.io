---
title : "[Scala 1] Types & Classes"
tags: Scala
---

# Intro
앞서 Scala의 기본적인 문법과 기초 개념을 대충 살펴보았다. 이번엔 타입, 클래스, 객체들에 대해 간단히 알아보고, 마지막으로 패턴 매칭(pattern matching)까지 짚고 넘어가자.


# Types

![](/imgs/scala/1.png)

전에 언급하였듯, Scala에서는 기본적으로 위와 같은 구조를 가진다. `Any`, `AnyVal`, `AnyRef`, `Nothing`과 같은 몇 가지 특별한 타입이 있다. 상위 타입들은 하위 타입들에 대한 일반적이고 범용적인 접근과 메소드의 사용이 가능하다. 예를 들어, `toString()`은 Int, Short, Char 등의 타입들이 같이 쓰기를 원할 것이다. 

```scala
val x = 35
val y = 15
val z: Char = 'a'
println (x.toString() + y.toString() + z.toString()) // 3515a
```

상위 타입으로의 명시도 가능하다.

```scala
val x = 35
val y = 15
val z: Char = 'a'
println (x.toString() + y.toString() + z.toString()) // 57abca
```

타입을 이해할 때 알아야 할 사실이 있다. 바로 모든 타입은 클래스 기반으로 정의되고, 모든 타입이 객체라는 점이다. 또, 모든 클래스는 `Any`의 서브클래스이다. 잘 기억해놓자.


## Value Type
위 그림에서 볼 수 있듯이, 값 타입은 총 9 종류가 있다. 대부분은 친숙한 타입들이다. 그 중 Unit은 오직 하나의 정보만을 가질 수 있는(Scala에선 `()`로 표현된다), 의미 없는 정보를 가지는 타입이다. Python이 `NoneType`은 `None`이라는 값만 가질 수 있는 것과 비슷한 맥락이다.

### Type Casting
Scala에선 Type casting이 지원되지만, 단방향성으로만 이루어진다.

![](/imgs/scala/2.png)

가령, 아래 코드에서 마지막 줄은 오류를 발생시킨다.

```scala
val x: Byte = 31
val y: Int = x
val z: Float = y
val err: Long = z 
```

## Reference Type
참조 타입은 값 타입의 여집합이다. 별 다른 조치가 없다면, 사용자 정의 클래스는 기본적으로 참조 타입이 되며, 그에 따라 `AnyRef`의 서브클래스가 된다.

### Options
옵션(option)은 특정 장소에서의 값의 존재 여부를 나타내기 위한 타입이다. 나중에 사용할 일이 생길 때 따로 다루어 볼 예정이다.

### Lists

```scala
// 선언과 참조
val intlist = List(1, 2, 3, 5)
println(intlist) // List(1, 2, 3, 5)
println(intlist(1)) // 2

val intlist2: List[Int] = List(2, 4, 5, 7) // 타입 지정
println(intlist2(3)) // 7

val intlist_err: List[Int] = List("Hello", "World") // 타입 미스매치에 의한 오류

val anylist1 = List("a", 'a', 3, 3, 5.7) // 여러 타입이 리스트의 원소가 될 수 있다.
val anylsit2: List[Any] = List('a', 3, 8.2) // 명시도 가능하다.
```

리스트를 이용한 몇 가지 기본적인 연산을 할 수 있다.

```scala
// :: 을 이용해 리스트 앞에 원소를 추가하는 연산을 할 수 있다.
val list0 = 0 :: List(1, 2, 3)
println(list0) // List(0, 1, 2, 3)


// :+ 을 이용해 리스트 뒤에 원소를 추가하는 연산을 할 수 있다.
val list1 = List("a", "b") :+ "c"
println(list1)


// ::: 을 이용해 리스트를 합칠 수 있다.
val list2 = List("a", "b", "c") ::: List(1, 2, 3)
println(list2) // List(a, b, c, 1, 2, 3)
```

메소드까지 알아보는 건 너무 의미가 없고, 필요할 때 알아서 찾아서 쓰자.


# Classes
## Class
이제 새로운 타입을 정의하기 위해, 클래스를 사용해보자. 기본적으로 다른 언어와 그 방법이 유사해서, 딱히 어렵지는 않을 것이다.

예시로 정수 쌍 클래스를 하나 만들어보자.

```scala
class IntPair(var first: Int, var second: Int, val meta: Int = 1){

	// 멤버 정의하기
	val meta1: Int = 0 // 기본적으로 public이다.
	private val meta2 = Int = 1
	protected val meta3 = Int = 2


	// 메서드 정의하기
	def print_pair: Unit = println(s"(${first}, ${second})")
	
	def ret_pair: String = s"(${first}, ${second})"

	def x_plus_n(n: Int): Int = first + n
	def y_plus_n(n: Int): Int = second + n

	def change_x(n: Int): Unit = {first = n}
	def change_y(n: Int): Unit = {second = n}
}

// 인스턴스 생성 후 사용하기
val pair1 = new IntPair(2, 3)
pair1.print_pair // (2,3)
println(pair1.ret_pair) // (2, 3)
println(s"${pair1.x_plus_n(3)} ${pair1.y_plus_n(14)}") // 5 17

pair1.change_x(15)
println(pair1.first) // 15
```

### Constructor
위에서 알 수 있듯, `new` 키워드를 이용해 새로운 인스턴스를 생성할 수 있다. 이 때, 파라미터를 받을 수도 있고, 그렇지 않을 수도 있다. 기본값을 지정하는 것도, 인스턴스 생성 시 파라미터를 특정하여 값을 할당하는 것도 가능하다.

Scala엔 별도의 생성자가 없지만, 메서드 외의 코드들이 생성자와 같이 동작한다.

```scala
class Yo(val x: Int, val y: Int = 2, val z: Int = 5)

val yoyo = new Yo(3, z=15)
println(s"${yoyo.x} ${yoyo.y} ${yoyo.z}")
```

### Case Classes
`case` 키워드를 사용해 케이스 클래스를 정의할 수 있다.

```scala
case class Ho(x: Int, y: Int)
```

이렇게 만든 클래스는 다음과 같은 특징을 가진다.

- `new` 키워드 없이 인스턴스를 생성할 수 있다.

```scala
val hoho1 =  Ho(1, 2)
val hoho2 = Ho(35, 27)
```

- 비교 시 레퍼런스가 아닌, 내부 구조를 비교한다. (compared by value)

```scala
case class Ho1(x: Int, y: Int)
class Ho2(x: Int, y: Int)
case class Ho3(x: Int, y: Int)

val hoho1 = Ho1(2, 3)
val hoho2 = Ho1(2, 3)
val hoho3 = new Ho2(2, 3)
val hoho4 = new Ho2(2, 3)
val hoho5 = Ho3(2, 3)

println(s"${hoho1 == hoho2} ${hoho3 == hoho4}") // true false
println(s"${hoho1 == hoho5}") // 믈론, 이 경우엔 false다.
```

- 반드시 파라미터 리스트를 가져야 한다. (비어있더라도)

케이스 클래스는 여러 측면에서 유용한데, 지금은 넘어가고 나중에 필요할 때 다시 쓰자.

## Objects
오브젝트는 간단히 말하면 singleton instance다. 전역적으로 참조될 수 있기에, 다양한 방식으로 활용될 수 있다.

예를 들어, 여러 클래스들의 인스턴스를 카운트하고 싶다면?

```scala
object Counter {
	private var counter: Int = 0
	def count: Unit = counter += 1
	def get_count: Int = counter
}

class Class1(x: Int){
	Counter.count
}
class Class2(y: String){
	Counter.count
}

val c1 = new Class1(35)
val c2 = new Class2("helllo")
println(Counter.get_count) // 2
```

## Trait & Inheritance
Trait을 이용해 우리는 ADT를 정의할 수 있다. 이는 공통된 변수, 메서드 등의 상속을 할 때 유용하다. 단, 이는 abstract class이므로 인스턴스 생성(instantiate)이 불가능하다.

```scala
trait Plus {
	def printnum(n: Int): Unit = println(n)
}

// extends 키워드를 이용해 상속한다.
class Class1 extends Plus
val c1 = new Class1
c1.printnum(35) // 35

// override 키워드를 이용해 덮어쓸 수 있다. Polymorphism!
class Class2 extends Plus{
  override def printnum(n: Int): Unit = println(s"Your number is ${n}")
}
val c2 = new Class2
c2.printnum(35) // Your nnumber is 35

// 물론, 이는 불가능하다.
class Class3 extends Plus{
  override def printnum(n: Int ,m: Int) = println(n, m)
}
```


# Pattern Matching
## Inductive Data Types: List
패턴 매칭 이전에, 좀 뜬금없지만 데이터 타입을 귀납적으로 정의해보자. 우리가 정의할 대상은 리스트다.

리스트는 (axiom에 의해 리스트 집합에 속하는) 빈 리스트(`nil`)에서 시작하여, 리스트 집합과 어떤 한 원소를 합친 것도 리스트라고 정함으로써 정의된다. 가령 정수 리스트를 예시로 한다면,

> $l \to nil \vert n \bullet l, n \in \Bbb{Z}$

이를 직접 구현해보자.

```scala
trait IntList
case class Nil() extends IntList
case class Ext(ele: Int, list: IntList) extends IntList

val nil = Nil() // []
val a = Ext(1, Nil()) // [1]
val b = Ext(2, a) // [2, 1]
val c = Ext(3, b) // [3, 2, 1]
println(c) // Ext(3, Ext(2, Ext(1, Nil())))

println(nil.isInstanceOf[IntList]) // true
println(nil.isInstanceOf[Ext]) // false
println(nil.isInstanceOf[Nil]) // true 
println(c.isInstanceOf[IntList]) // true
println(c.isInstanceOf[Ext]) // true
println(c.isInstanceOf[Nil]) // false
```

## Pattern Matching
Scala는 패턴 매칭을 지원한다. `match`를 사용하여 다양한 케이스에서의 패턴 매칭을 시도하고, 매칭 시 그에 맞는 표현식을 실행한다. 위에서 만든 리스트를 문자열로 깔끔하게 나타내는 메서드를 만들어보자.

```scala
def str(l: IntList): String = l match {
  case Ext(ele, list) => ele.toString() + " " + str(list)
  case _ => "" // 와일드카드
}

println(str(Ext(1, Ext(2, Ext(3, Ext(4, Ext(5, Nil()))))))) // 1 2 3 4 5
```

정리하면, 다음과 같은 문법으로 사용한다.

```scala
(expression) match {
	case (pattern) => (expression)
	...
	}
```

패턴 매칭은 검사의 방법이 매우 다양하다는 장점을 가진다. 데이터 타입을 검사할 수도, 값을 검사할 수도 있다. 매칭되는 케이스가 없으면 매치 에러를 발생시킨다는 점을 주의하자.

사실 패턴 매칭은 할 말이 무척 많은 주제지만, 바빠서 빨리 진도 나가야해서 나중에 자세히 살펴보는 걸로...