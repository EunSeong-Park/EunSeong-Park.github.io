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

```Scala
1+1
"hi"
'a'
```

등은 모두 표현식으로 볼 수 있다. 표현식은 `println` 함수에 의해 콘솔에서 출력될 수 있다.

```Scala
println(1024)
println(5 * 5)
```

이제, `println`을 이용해 `Hello, World!`를 여러 방법으로 출력해보자.

```Scala
println("Hello, World!")
println("Hello, " + "World!")
```

위에서 볼 수 있듯, (Python 처럼) 문자열의 concatenation이 가능하다. 와, 편리하다!

