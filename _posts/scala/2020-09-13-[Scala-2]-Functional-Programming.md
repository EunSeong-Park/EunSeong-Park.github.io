---
title : "[Scala 2] Functional Programming Basic"
tags: Scala
---

# Intro
드디어 함수형 프로그래밍에 대해 알아볼 차례다. 오예~


# Functional Programming
결국 함수형 프로그래밍도 (객체 지향, 명령형 등과 같은) 프로그래밍의 패러다임(paradigm) 중 하나다. 그럼, 어떤 것을 함수형 프로그래밍이라 부를까?

1. 계산(computation)을 수학적 함수들의 조합으로 본다.
2. Side-effect가 없이 output(return value)만을 계산하기 위한, pure한 함수들로 프로그램을 구성한다.
3. 불변(immutable) 데이터를 통해 작업한다.


## Advantages
### Modularity
함수형 프로그래밍에선 문제가 작은 조각들로 나누어지고, 각각은 pure한 작은 함수들에 의해 해결되며, 이들이 결합하고 잘 구조화되어 프로그램의 목적이 달성된다. 이러한 시도로 프로그램은 고도로 모듈화되고, 이는 디버깅, 가독성, 유지 보수 등 여러 측면에서 유리하다.

### Debug / Test
함수형 프로그램은 테스트와 디버깅이 용이하다. 모듈화된 작은 함수들은 그 기능과 효과가 분명하기 때문에 더 단순해지고, 시스템 상태에 의존하지 않으므로 우리는 입력에 대한 출력의 상태만 확인하면 된다.

### Formal Provability
프로그램을 수학적 함수의 조합으로 바라볼 수 있기 때문에, 프로그램이 옳은 결과를 리턴한다는 사실을 형식적으로 증명할 수 있다. 코드를 읽고, 여러 테스트 케이스를 대입하는 것보다 더욱 엄격한 확증이 가능해진다.

### Composability
작게 모듈화된 함수는 그 프로그램에만 국한되지 않고, 라이브러리화되어 효율적으로 사용될 수 있다.

# Features
## Pure Function
두 함수를 살펴보자.

```c
int add_1(int * a){
	a += 1;
	return a;
}

int add_1_pure(int a){
	return a + 1;
}
```
`add_1`은 `*a`에 있는 데이터를 바꾸지만, `add_1_pure`는 상태(state)를 변경하지 않고 오로지 리턴값의 계산만을 수행한다. 우리는 함수형 프로그래밍에서, pure function만을 사용할 것이다. 또, 그에 따라, mutable한 변수 또한 쓸 필요가 없을 것이다.

또한, pure function은 상태를 변경하지 않을 뿐 아니라, 외부 상태에 의해 영향을 받지도 않아야 한다. 즉, 같은 input이면 항상 같은 output을 내놓아야 한다. 


## First-Class / Higher-Order Function
함수를 input(parameter)이나 return value로 가질 수 있는 함수들을 higher-order하다고 한다. 어? 이거 조금 1급 함수랑 비슷하지 않나? 싶은데, 이 또한 정리해보자.

1. **First-class function**: 함수는 (다른 타입이 그렇듯) 표현식의 일종으로 작용하여, 어떤 함수를 파라미터, 리턴 값으로 사용할 수 있다. 또, 함수를 변수나 다른 데이터 구조에 할당하는 것도 가능하다.
2. **Higher-order function**: 함수를 파라미터 / 리턴 값으로 사용할 수 있다. 

결국 1급 함수의 부분집합 정도로 봐도 무방한 셈이다. 이렇게 일반화된 함수는 매우 다양한 방법으로 활용될 수 있다. 그런데, Scala에선 어떨까?

```scala
// 데이터 구조에 함수를 할당할 수 있다.
val addone = (x: Int) => x + 1
val addtwo = (x: Int) => x + 2

val addoneone = addone 
val addlist = List(addone, addtwo) // 리스트에도 할당 가능하다.

println(addone(5)) // 6
println(addoneone(5)) // 6
println(addlist(0)(2), addlist(1)(3)) // (3,5)


// 함수를 파라미터로 사용할 수 있다.
val moreadder = (adder: (Int) => Int, x: Int) => adder(x) + 1

println(moreadder(addone, 4)) // 6


// 함수를 리턴값으로 사용할 수 있다.
def sumup(n: Int): Int = if (n >= 1) n + sumup(n-1) else 0

println(sumup(100))
```

이러한 특징은 함수의 reusability를 향상시켜준다. 예를 들어, $x^3 + y^3 + z^3$을 계산하는 함수를 만든다고 해보자.

```scala
def naive(x: Int, y: Int, z: Int): Int = x * x * x + y * y * y + z * z * z

println(naive(1,2,3)) // 36
```

이렇게 다시 작성하면 어떨까?

```scala
def cube(x: Int): Int = x * x * x
def better(x: Int, y: Int, z: Int) = cube(x) + cube(y) + cube(z)

println(better(1,2,3)) // 36
```

## Closures
클로저(closure)를 알기 위해, 먼저 예시를 살펴보자.

```scala
var tip = 1000
val price = (x: Int) => x + tip
```

여기서 우린 `tip`과 `x`에 주목하자. `x`는 그 함수에 귀속되어 있고, 그 스코프 내에서 유효하다. 하지만 `tip`은 다른데, 함수 밖에서 정의되고, 그렇기에 그 값이 변경될 수 있다. 이 때, `price`를 클로저(closure)라고 부른다.

여기서 흥미로운 점이 있는데, 클로저는 이렇게 스코프 밖에서 정의된 변수에 대해, 그 변수 자체를 가져옴으로써 (not value) 외부 변화에 반응할 수 있다. 예를 들어,

```scala
var tip = 1000
val price = (x: Int) => x + tip

println(price(5000)) // 6000

tip = 2000
println(price(5000)) // 7000
```

## Loop
맨 앞의 내용을 떠올려보면, Scala는 `var` 사용을 지양하는 방향으로 사용될 것을 권장하는 것 같다. 그런데 대부분의 루프가 counter variable이 있다는 점을 생각하면, 루프 사용도 권장되지 않는 게 아닌가?

그래서 우리는 대신 재귀(recursion)를 사용한다. 띠용? 패턴 매칭 등을 통해 대부분의 문제를 재귀로 해결할 수 있긴 하다. 하지만 너무 깊은 재귀는 스택을 터뜨린다는 걱정이 있을 것이다. 이는 tail-recursion을 이용해 스택을 재사용하는 것으로 해결한다.

루프의 재귀로의 변환, tail-recursion 등은 이미 배운 내용이고, 지엽적인 부분이라 생각해 넘어간다.
