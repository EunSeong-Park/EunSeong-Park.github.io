---
title: "[Data Science Programming 2] Intro to Python"
tags: Data-Science Statistics Python
toc: true
---

# Intro
우선, 여기선 Python을 사용할 예정이므로, 기본적인 관련 지식을 충분히 확인하고 가도록 하자. Python의 기본적인 특징과, 아주 기초적인 요소들을 알아볼 것이다. 어째 초등학생용 파이썬 강좌같다...

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
inventory = {
    'ham': 10,
    'onion': 5,
    'bread': 2,
    'meat': 10
}
print(inventory['ham'])             # 10
print(list(inventory.items())[2])   # ('bread', 2)

```

## Conditionals / Loops
### Conditionals
`if`, `else`, `elif`에 의해 conditional execution이 수행된다. 다 아는 내용이므로 디테일은 생략한다.

```python
if False:     # if / elif 뒤엔 bool이나 bool로 변환될 수 있는 무언가가 온다.
    pass      # 아무것도 하고 싶지 않을 때
elif (None and False) or (0 and 1):
    print("no way~")
else:
    print("done")  
```

### Loops
`for`, `while`을 사용하여 반복문을 만들 수 있다.

```python
sum = 0
# for (iterator) in (iterable object such as list, range, string, etc.)
for i in range(1,101): # range(<start>, end, <steps>): start부터 end-1까지
    sum += i
print(i)    # 5050

k = 0
# while (condition): 루프 한 바퀴마다 condition을 검사하고, True면 내부 블록 실행 
while True:
    k += 1
    if k == 50:
        break    # 조건과 상관없이 루프를 탈출
    else:
        continue # 바로 다음 iteration으로 넘어감

```

## Function Basics
이제 함수를 정의해보자, `def` 키워드로 할 수 있다.

```python
def my_abs(x):
    if x < 0:
        return -1 * x
    else:
        return x

print(my_abs(-1)) # 1
```

리턴 타입을 지정할 필요는 없으며, 한 함수가 경우에 따라 여러 종류의 타입을 리턴할 수도 있다.

파라미터의 기본값을 지정할 수도 있다. 기본값이 지정되어있다면 호출 시 생략 가능하다.

```python
def my_print(string="Nothing"):
    print(string)

my_print()      # Nothing
my_print("yo")  # yo
```

`*args`, `**kwargs`를 사용해보자. 전자는 non-keyworded argument를, 후자는 keyworded argument를 받는다. 가변적인 길이로 받을 수 있다는 게 주 특징이다. `args`는 튜플 형태로, `kwargs`는 딕셔너리 형태로 함수에 들어온다. 일반적으로 저 이름을 쓰는 게 convention이긴 하지만, 굳이 저 이름을 쓸 필욘 없다.

```python
def my_function(arg1, arg2, *args, **kwargs):
    print(arg1, arg2)
    print(args)
    print(kwargs)

my_function(1,2,3,4,5,a=6,b=7,c=8) 
# 1 2
# (3, 4, 5)
# {'a': 6, 'b': 7, 'c': 8}
```

`lambda` 키워드를 사용해, 함수를 개별 객체로 사용할 수 있다. 함수형 프로그래밍 패러다임을 위해 사용할 수 있다.

```python
adder = lambda x, y: x + y
adder(1,2)  # 3

def power_generator(pow):
    return lambda x: x ** pow

pow2 = power_generator(2)
pow3 = power_generator(3)
print(pow2(5), pow3(5)) # 25 125
```

## Class
**클래스(class)**는 간단히 말하면 사용자 지정 타입이자, (멤버) 변수와 함수들의 그룹이기도 하다. 옛날에 객체 지향 패러다임을 배웠을 테니 클래스의 장점과 기능은 생략한다.

아무튼, 클래스는 보통 다음과 같이 사용된다. 예시를 보자.

```python
# class definition
class Student:
    
    # member function (method)
    def __init__(self, name, ID): # constructor
        # member variable
        self.name = name
        self.ID = ID
        self.GPA = 0.0

    def rename(self, name): # change the name
        self.name = name
    def get_ID(self): # get ID
        return self.ID

x = Student("Eunseong", 20181098)

print(x.name)       # Eunseong
print(x.get_ID())   # 20181098
```

### Special Methods
클래스에 제공되는 몇 가지 특별한 메소드가 있다. 더블 언더스코어(__)에 감싸진 메소드가 그렇다. 자주 사용하는 애들만 보자.

- `__init__`: 객체 생성 시 (정확히는 `__new__` 호출 이후) 실행되는 메소드. 멤버 변수 초기화 등에 사용할 수 있다.
- `__del__`: `del` 키워드 등에 의해 객체 소멸 시 호출되는 메소드. 
- `__str__`: 객체에 대응되는 문자열을 반환하는 메소드. `str(object)` 호출 시 이 메소드가 리턴하는 값을 리턴한다.
- `__len__`: 객체에 대응되는 길이($\ge 0$)를 반환하는 메소드. `len(object)` 호출 시 이 메소드가 리턴하는 값을 리턴한다.

### Access Modifiers
대부분의 OOP 지원 언어가 그렇듯, 멤버를 `public`, `private`, `protected`하게 지정할 수 있다. 왜 필요한지는 다들 알 테니 생략하지만, 각각이 뭘 의미하는지는 다시 떠올려보자!

- `public`: 멤버는 완전히 공개되어, 객체를 사용하는 외부에서 해당 멤버에 접근할 수 있다.
- `private`: 멤버는 비공개되어, 클래스 내부에서만 접근될 수 있다.
- `protected`: 멤버는 외부에게 비공개되며, 클래스 내부와 자식 클래스에 의해서만 접근될 수 있다. 하지만 외부에서의 접근 제한은 강제되지 않고, 경고를 출력할 뿐이다.

이들을 위한 별도의 키워드는 없고, 멤버 이름, `mem`에 대한 네이밍으로 access modifier를 결정한다.

Naming | Access
---|---
`mem` | Public
`_mem` | Protected
`__mem` | Private

