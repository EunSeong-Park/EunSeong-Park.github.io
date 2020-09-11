---
title : "[Scala 1] Types & Classes & Objects"
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


# Class
이제 새로운 타입을 정의하기 위해, 클래스를 사용해보자. 기본적으로 다른 언어와 그 방법이 유사해서, 딱히 어렵지는 않을 것이다.

예시로 정수 쌍 클래스를 하나 만들어보자.

```scala
// 클래스 정의하기
class IntPair(first: Int, second: Int){
	def print_pair: Unit = {println("(" + first + ", " second + ")")}
	def change
}

// 인스턴스 생성 후 사용하기
val pair1 = new IntPair(2, 3)
pair1.print_pair()
```