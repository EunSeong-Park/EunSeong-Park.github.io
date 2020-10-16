---
title: "[Data Science Programming 2] Intro to Python"
tags: Data-Science Statistics Python
toc: true
---

# Intro
우선, 여기선 Python을 사용할 예정이므로, 기본적인 관련 지식을 충분히 확인하고 가도록 하자. Python의 기본적인 특징과, 자료형(data type), 제어문 등을 알아볼 것이다. 이러니까 초등학생용 파이썬 강좌같다...

아, 그리고 여기선 Python 3.8을 사용할 예정이다. 아무튼 시작!

# Python
**Python**은 오픈소스인 zl존짱짱 언어라고 할 수 있다. High-level 프로그래밍 언어 중에서도 고도의 편의성을 제공하며, 다양한 programming paradigm을 지원한다. 인기가 많은 언어여서 별별 라이브러리가 있다는 것도 장점이다. 

몇 가지 기본적인 특징을 알아볼까?

- **Indent-sensitive**: 다른 많은 언어와 달리, Python은 들여쓰기(indent)에 민감하다. 들여쓰기에 의해 코드 블록들이 묶이고 구조화된다. 
- **Dynamic data type**: 자료형은 런타임에서 검사된다. 또, 특정 변수의 자료형이 도중에 바뀔 수도 있다.
- **Interpreter language**: Python은 인터프리터 언어, 그 중에서도 대화형 인터프리터 언어다.
- **Fast to develop**: Python은 그 특유의 간결함과 편리함으로 인해, 전반적으로 개발 속도가 빠르다.
- **Memory management**: Python에선 자동적으로 메모리를 관리해준다. `malloc()`, `free()`와 같은 짓을 안해도 된다!

# Python Basics
## Data Types
Python은 수많은 종류의 기본적인 자료형을 제공한다.

- **Numeric types**: integer, float, boolean
- **Sequence types**:  string, tuple, range, list
- **Set type**:  set  
- **Mapping type**: dictionary

변수는 `(var_name) = (var_value)`와 같은 방식으로 선언한다. 여기서 중요한 건, **반드시 명시적으로 자료형을 나타낼 필요는 없다**는 점이다.

변수명은 `[a-z]`, `[A-Z]`, `[0-9]`, `_`로 구성된다. 단, 숫자는 변수명 맨 앞에 올 수 없음을 유의하자.

### Numeric Types
```python
x = 1       # type: int
y = 1.2     # type: float
z = True    # type: bool
```

어떤 변수의 타입을 확인하고 싶다면, `type()`함수를 사용하자.

```python
print(type(x)) # int
print(type(y)) # float
print(type(z)) # bool
```

당연하게도, 특정 연산의 결과를 변수에 바로 할당할 수도 있다.

```python
w = 5 + 10          # 15
x = 5 / 2           # 2.5 (float)
y = 5 // 2          # 2 (int)
z = True or False   # True (bool)
```

`int()`, `float()`, `bool()` 등의 함수는 주어진 파라미터를 해당 타입으로 변환해준다. 물론, 유효한 형태의 변환이어야 한다.

```python
w = bool(15)        # True (if 0/None/False/etc then False, otherwise True)
x = int(155.5)      # 155
y = float(100)      # 100.0
z = int(True)       # 1
```

### Sequences
List, string, tuple은 대표적인 시퀀스(sequence)타입이다. 보통 다음과 같은 공통적인 오퍼레이션을 제공한다.

- **Indexing**: `seq[i]`는 `seq` 내의 `i`번째 원소에 대응된다.
- **slicing**: `seq[i:j]`는 `seq` 내의 `i`번째부터 `j-1`번째까지의 sub-sequence에 대응된다.

또, 시퀀스 간의 `+`, `-`, 어떤 정수에 대한 `*` 연산자가 정의되며, 특정 원소의 존재성을 찾기 위한 `in`, `not in`이 제공된다(bool 타입을 반환). 또, 공통적으로 해당 시퀀스의 길이를 리턴하는 `len()`함수도 지원한다.

이제부터 각각에 대해 알아볼 예정인데, 이들이 지원하는 메소드는 꽤 지엽적인 부분이기도 하고, 여기서 쓸 일은 별로 없기도 하고, 어차피 구글 치면 다 나오므로 그냥 생략한다.

**문자열(string)**은 말 그대로 글자들의 sequence다. Python은 별도로 `char` 타입을 가지지 않는다는 점을 기억하자.

```python
s1 = "Hello"
s2 = str(155)   # str() 함수를 이용해 문자열로 변환이 가능하다.
print(s1[4])    # o
print(s1[1:3])  # el
print(s1[2:])   # llo
```

**튜플(tuple)**은 임의의 타입을 가진 원소들을 포함하는 시퀀스다. 선언된 이후엔 변경이 불가능한 immutable class다.

```python
t1 = ()                     # declaration 1
t2 = (3, "ta", True, 12)    # declaration 2
t3 = (5, 'oooo') + t2       # declaration 3

t2[1] = 5                   # Thid doesn't work
```

**리스트(list)**는 튜플과 비슷하지만, mutable class라는 점에서 다르다.

```python
l1 = []                               # declaration 1 
l2 = [[], [], (), l1, "a", 32]        # declaration 2
l3 = [[[1, 2, [[], []]], "d"], []]    # 얼마든지 nested해질 수 있다.

l1.append(15)   # 리스트는 mutable하다.
l1[0] = 16
l1.remove(16)
```

### Set
**집합(set)**은 수학에서 쓰는 그것과 유사하다. 순서를 신경쓰지 않고, 중복된 원소는 reduce된다는 특징을 가지고 있다. 합집합(union, `|`), 교집합(intersection, `&`), 차집합(subtraction, `-`)을 위한 연산을 제공한다.

```python
a = {1,1,1,2,3}     # {1,2,3}
b = {3,4,5,6,6}     # {3,4,5,6}   
c = set([1,2,3,3])  # {1,2,3}

print(a&b)          # {3}
print(a|b)          # {1,2,3,4,5,6}
print((a|b) - c)    # {4,5,6}
```

### Dictionary
**딕셔너리(dictionary)**는 해시 테이블(hash table), 혹은 맵(map)의 역할을 하는 자료형이다. 각 원소는 `(key, value)` 쌍으로 구성되며, `key`는 딕셔너리 내에서 유일하나, `value`는 그럴 필요는 없다.

```python

```