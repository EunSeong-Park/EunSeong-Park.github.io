---
title : "[Scala 0] Intro & Basics"
tags: Scala
---

# Intro
__Scala__ 는 Object-oriented한 성질과 functional한 성질을 함께 가지는 프로그래밍 언어다. Scala는 컴파일러에 의해 JVM에서 실행되며, 이에 따라 Java와 잘 호환된다. (상대적으로) 덜 인기있고 덜 개발된 Scala의 단점을 보완해준다고 볼 수 있겠다.

그런데 왜 갑자기 Scala를 시작하냐? 하면, 학교에서 Scala를 쓰고 있기 때문이다.(...) 난 Java도 제대로 써본 적이 없어 Scala와 Java와의 연계는 생각도 못해보고, Scala는 지금 배우는 중이라 부실하거나 잘못된 이해를 할 수도 있다. 아무도 이 블로그를 보지 않는다는 사실이 다행이다.

코스 관련 과제나 프로젝트는 올리는 게 금지되어 있기 때문에, Scala 자체만을 정리할 예정이다.


# Features
프로그래밍 언어로서의 Scala는 다음과 같은 특징들을 가진다.

1. Functional language
2. Value-oriented language
3. Type inference
4. Pattern matching

각각의 특성이 정확히 무엇인지, 그러한 특성은 코드 작성과 개발 시 어떤 영향을 주는지는 나중에 알아보자. 직접 Scala를 사용하면서 이들을 느낄 수 있을 거라고 생각한다.


# Basics
여기서는 [scalafiddle.io](https://scalafiddle.io/)에서 코드를 돌릴 예정이다. Scala 버전은 2.12, Scala.js 버전은 0.6.x를 사용한다.

## Expressions & Hello, World!
표현식(expression)은 연산 가능한 명령문이자 코드 조각이다. 가령,

```scala
1+1
"hi"
'a'
```

등은 모두 표현식으로 볼 수 있다. 표현식은 `println` 함수에 의해 콘솔에서 출력될 수 있다.

```scala
println(1024)
println(5 * 5)
```

이제, `println`을 이용해 `Hello, World!`를 여러 방법으로 출력해보자.

```scala
println("Hello, World!")
println("Hello, " + "World!")
```

위에서 볼 수 있듯, (Python 처럼) 문자열의 concatenation이 가능하다. 와, 편리하다!

## `println`
주로 `println`을 사용하겠지만, `print`, `printf` 또한 사용 가능하다! 하지만 이들이 동작하는 방식(개행 여부, 타입 등)은 꽤 다르다. `println`은 Python의 `print`만큼 편리하다. 왜냐? `println`은 모든 타입을 적절히 처리하여 출력할 수 있기 때문이다. (가령 `printf(35)` 같은 코드는 type mismatch에 의한 오류를 발생시킨다.)

## Value & Variable
값(value)은 `val` 키워드에 의해, 변수(variable)는 `var` 키워드에 의해 선언된다.

```scala
val x = 1	
val y = 3 + 8	// 표현식으로도 값을 선언할 수 있다.
println(y)		// 11
```

값은 reassignment가 불가능한, immutable한 특성을 가지고 있다. 즉, 위와 같은 코드를 실행시킨 뒤,  `x = 5`처럼 값을 수정할 수 없다. (오류를 발생시킨다)

```scala
var x = 1024
x = 3
println(x)
```

변수는 mutable하기 때문에, 위와 같은 코드가 오류를 발생시키지 않는다.

## Types
### Static / Dynamic Types
Scala에서의 타입을 알아보기 전, 정적(static) 타입과 동적(dynamic) 타입에 대해 알아보자. 

- 정적 타입: 컴파일 단계에서 타입을 확인한다. 
- 동적 타입: 런타임 단계에서 타입을 확인한다.

Scala, C, C++ 등은 정적 타입 언어다. 타입 에러를 비교적 일찍 검출할 수 있고, 런타임 체크가 필요없으므로 조금 더 빠르다. 그 중에서도 Scala는 type-safe한 성질을 가지고 있다. (C/C++과 달리) 런타임에서 타입 에러가 발생하지 않음을 보장한다.

반면, Python, JavaScript 등은 동적 타입 언어다. 더 유연하지만, 런타임, 혹은 deployment가 끝난 이후에도 타입 에러를 볼 수 있다는 단점이 있다.

### Scala Types

![](/imgs/scala/01.png)

Scala에서의 모든 데이터는 타입에 대응한다. 최상위(root) 타입으로 `Any`가 있고, 이는 value type인 `AnyVal`과 reference type인 `AnyRef`이란 서브 타입들로 나눌 수 있다. 상위 타입은 그것의 서브 타입을 위한 메소드를 포함한다. (예를 들어, `toString`은 Int에서도, Short에서도 사용할 것이다.)

타입은 나중에 자세히 다루도록 한다. 당분간은 value type만 사용할 예정이고, 각각은 다른 언어들과 큰 차이가 없다. 가령 Int가 32비티를 사용하는 것 같이..

### Type Inference / Specification
컴파일러는 기본적으로 값이나 변수에 할당된 값을 보고 이를 적절한 타입으로 추론한다. 이를 type inference라고 한다. (파이썬을 생각하면 쉽다.) 반면, 타입을 직접적으로 명시할 수도 있다.

```scala
val x: Int = 15
val y: String = "Hello, World!"
val z: Boolean = (true || false) && true
```

위처럼, `(name):(type) = (expression)`와 같은 형식으로 명시하면 된다.

## String Interpolation
Scala는 데이터를 문자열 내에서 표현할 수 있도록 하는, 문자열의 보간(interpolation)을 지원한다. 예시를 우선 확인해보자.

```scala
val a = 35
println(s"a's value = $a")
println(s"a's value = ${a}")
```

거의 모든 표현식이 보간의 대상이 될 수 있다.

보간도 여러 방법이 있지만, 여기선 `s` / `f` 인터폴레이터에 의한 보간만을 알아본다.

### `s` Interpolator
`s` 인터폴레이터를 사용하면 변수나 값을 직접적으로 문자열에 보간시킬 수 있다.

```scala
val x = 3
val y = s"x is ${x}"
println(s"$x ${x} $y ${55 + 5}")
```

### `f` Interpolator
`f` 인터폴레이터는 다른 언어의 `printf`의 동작 방식과 비슷하다. `%d`와 같은 포맷 스트링을 사용할 수 있다.

```scala
val x = 15
val y = "Hello"
val z = 1.234
println(f" $x \t $y \t $z%f \t $z%.2f")
```

## Block
블록(block)은 여러 개의 표현식을 감쌀 수 있다. Curly bracket(`{`, `}`)으로 표현한다.

블록은 __마지막 줄의 표현식의 값을 가진다.__ 이것이 (러프하게 말하면) 블록의 리턴값이라고 볼 수도 있을 것 같다.
```scala
println({
	val x = 1 + 1
	x + 1
	x + 2
})
```
`println`은 위 코드는 정확히 `3`을 출력한다.

여기서, 값 `x`는 블록 내에서만 유효하다. Scope에 유의하자.

```scala
val x = {
  val y = 1
  y+1
}
println(x) // 2
println(y) // Error (not found)
```

# Functions / Methods
## Functions
함수는 파라미터를 가지는 __표현식__ 이다. `=>` 를 사용하여, 그것의 왼쪽에 받을 파라미터를, 오른쪽에 그 함수가 가질 값의 표현식을 명시한다.

물론, 여러 파라미터를 받을 수 있다.

```scala
val add1 = (x: Int) => x + 1
val add2 = (x: Int, y: Int) => x + y
println(s"${add1(1)} ${add2(1, 2)}") // 2 3
```

파라미터의 타입을 명시해주어야 한다는 점을 주의하자. Type Safety!

```scala
// 블록 또한 사용할 수 있다.
println({ 
	val add = (x: Int) => {
	x + 1
	x + 2
	}
	add(7)
})


// 값이 아닌, 변수로 사용할 수도 있다.
var add1 = (x: Int) => x + 1
add1 = (x: Int) => x + 2

println(add1(0)) // 2


// 파라미터를 생략할 수도 있다.
println({
	val get1 = () => 1
	get1()
})
```

## Methods
Scala에서 메소드는 우리가 다른 언어에서 사용하는 언어와 조금 더 비슷한 것처럼 보인다. (주관적인 생각이다) 함수와 비슷하게 동작하지만, 몇 가지 측면에선 다르다. 여기선 자세히 다루지 않고, 용법만을 알아볼 것이다. 우선, 메소드를 정의하는 것으로 시작해보자.

```scala
def add(x: Int): Int = x + 1
println(add(1))
```

위처럼, `[Name](Paramter): (Return Type) (Body)`와 같은 형식으로 정의할 수 있다. 몇 가지 예제를 통해 그 특성을 알아보자.

```scala
// 물론, 여러 파라미터를 받을 수 있다.
def add(x: Int, y: Int): Int = x + y
println(add(1, 2)) // 3


// 여러 파라미터 리스트를 가질 수도 있다.
def linear(x: Int, y: Int)(a: Int): Int = a * x + y
println(linear(3, 5)(2)) // 11


// 파라미터 리스트를 아예 가지지 않을 수도 있다.
def noparam: Int = 1 + 2
println(noparam) // 3


// 타입 생략이 가능하다.
def infer(x: Int, y: Int) = x + y
println(infer(3, 2)) // 5

def noparam2 = 1 + 2
println(noparam2) // 3
```


# Conditionals
Scala에선 `if` 조차도 표현식이다. 와우! ... 그런데 어째서?

```scala
println({
	val x = if (true) 1 else 2
	val y = if (0 == 3) 2 else 1
	val z = if (true && true) 5
	val w = if (false) 5
	s"${x} ${y} ${z} ${w}"
}) // 1 1 5 undefined
```

결국 `if` 도 조건에 따라 값이 할당되는 표현식일 뿐이다. 여러 방법으로 조건식을 사용해보자.

```scala
val iseven = (num: Int) => if (num % 2 == 0) true else false
println(s"${iseven(1)} ${iseven(2048)}") // false true

println(
if (true) {
	val x = 5
	x + 4}
else {
	val y = 7
	y + 5
}) // 9
```
