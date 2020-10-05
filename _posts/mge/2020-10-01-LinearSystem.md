---
title: "Solving Linear System"
tags: Linear-Algebra Management-Engineering
toc: true
---

# Intro
간단한 linear algebra를 짚어보고 가자. 행렬 및 벡터에 대한 기초적인 개념과 그에 대한 여러 operation과 유용한 theorem들을 알아보고, 주어진 linear system을 해결하기 위한 방법들을 살펴볼 것이다.


# Vector
벡터(vector)는, 간단히 말하면 ordered $n$-tuple이다. 배열 방식에 따라 column vector와 row vector로 나눌 수 있겠지만, 여기선 별 다른 언급이 없는 한 column vector로 생각하자. 왜냐? linear system을 풀 때 더 자주, 유용하게 사용되기 때문이다. 하지만 표기할 땐 column vector가 더 편하긴 해서, $(x_1, x_2, x_3)^T$와 같은 표현을 종종 사용할 것이다.

몇 가지 특별한 벡터를 짚고 넘어가자.

- Zero vector: $\vec{0} = (0, 0, \cdots, 0)^T$
- Sum vector: $\vec{1} = (1, 1, \cdots, 1)^T$
- $i^{th}$ unit vector: $\vec{e_i} = (0, \cdots, 1 \;(i^{th}), \cdots, 0)$

다 알겠는데, 왜 $\vec{1}$은 sum vector로 부르냐? 하면, 같은 dimension의 row vector와 inner product를 하면 그 row vector의 모든 원소의 합이 되기 때문이다. 와! 아무튼 이처럼 이들은 여러 상황에서 유용하게 쓰일 수 있다.

## Vector Operation
별 다른 언급이 없다면 row / column vector 여부와 상관없이 일반적으로 적용된다.

### Addition
같은 차원의 두 벡터, $a = (a_1, a_2, \cdots, a_n)$, $b = (b_1, b_2, \cdots, b_n)$에 대하여, 덧셈을 다음과 같이 정의하자.

$a+b = (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$

### Scalar Multiplication
어떤 벡터 $a = (a_1, a_2, \cdots, a_n)$와 scalar, $k$에 대하여, scalar multiplication은 다음과 같이 정의된다.

$ka = (ka_1, ka_2, \cdots, ka_n)$

### Transpose
Row vector는 column vector로, column vector는 row vector로 뒤집어 변환한다. 벡터 $\vec{v}$에 대해, $\vec{v}^T$와 같이 표기한다.


### Inner Product
같은 차원의 두 벡터 $a = (a_1, a_2, \cdots, a_n)$와 $b = (b_1, b_2, \cdots, b_n)$에 대하여, inner product는 다음과 같이 정의된다. 한쪽은 row vector, 다른 한쪽은 column vector임을 유의하자.

$a^Tb = (a_1, a_2, \cdots, a_n)(b_1, b_2, \cdots, b_n)^T$ $= \sum_{i=1}^{n} a_i \cdot b_i$ $= b^Ta$


## Terminologies
### Norm
놈(norm)은 일반화된 벡터의 크기라 볼 수 있다.

$\Vert a \Vert = \sqrt{\sum_{i=1}^{n}a_i^2}$

### Linear Combination
선형 결합(linear combination)은 벡터 간의 addition과 scalar multiplication을 통해 새로운 벡터를 얻는 연산이다. 예를 들어, 2-dim에서 $e_1 = (1, 0)$과 $e_2 = (0,1)$, 그리고 scalar $k \in \mathbb R$를 이용한 선형 결합을 통해 우리는 (2-dim 안의) 임의의 벡터를 만들어낼 수 있을 것이다.

$(2, 7) = 2e_1 + 7e_2$

물론, 꼭 unit vector로 만들 필요는 없다. 어떤 벡터들은 그들의 선형 결합으로 그 차원 내의 모든 벡터를 얻을 수 있는 반면, 또 어떤 벡터들은 그렇지 않다. 가령, $(2, 1)$과 $(4,2)$로 $(7,3)$을 얻을 수 있을까?

여기서 중요한 주제가 있다. 선형 결합으로 모두를 만들어 낼 수 있는 벡터 집합과 그렇지 못한 벡터 집합은 어떤 성질이 달라서 이러한 차이를 만들어 낸 걸까? 

### Linear Independence
선형 독립성(linear independence)는 linear algebra에서 아주 중요한 성질 중 하나다. 선형 독립을 보이는 것만으로도 그들 자체와 그들이 구성하는 시스템에 대한 수 많은 특성을 이끌어낼 수 있기 때문이다. 

아니 그래서 선형 독립이 뭐냐? 하면... 다음과 같이 정의할 것이다.

> 어떤 벡터 집합 $ S = \{ a_1, a_2, \cdots, a_n \}은 다음과 같은 성질을 만족할 때, linearly independent하다고 한다: <br><br> $\sum_{i=1}^n k_ia_i = \vec{0} \implies k_i = 0 \text{ for all } i = 1, 2, \cdots n$

이게 뭔 개소리냐? 하면, 결국 이들로 zero vector를 만들려면 scalar가 모두 0이어야 한다는 이야기고, 대우로 다시 말하면, scalar가 0이 하나라도 아니면 이들은 반드시 zero vector가 아니어야 한다는 얘기다.

예를 들어, $n$개의 vector set이 종속적이어서 non-zero scalar로 zero vector를 만들었다고 치자. 그럼 하나의 벡터가 $\vec{a}$라면, 다른 나머지 모든 벡터의 합은 $-\vec{a}$일 것이다. (그래야 합이 zero vector니까!) 여기다가 방향만 반대로 하면($-1$), 나머지 벡터의 선형 결합으로 그 벡터, $\vec{a}$를 만들어낼 수 있는 셈이다.

이러한 측면에서, (조금 엄밀하지 못하지만) 선형 독립은 "집합($S$) 내의 벡터 부분집합($A \subset S$)의 선형 결합으로 그 외의 벡터($\vec{v} in (S-A)$)를 만들어낼 수 있는가?" 에 대한 답이 된다. 만들 수 있으면 종속이고, 그렇지 않으면 독립이다. 위의 예시에서 $(2, 1)$, $(4, 2)$는 어떨까? $2(2,1) = (4,2)$이므로 종속적이다. 원래 정의를 따르면, $-2(2,1) + (4,2) = \vec{0}$이므로 종속이라 할 수도 있겠다.

이제 선형 독립 여부를 판단하는 방법도 명확해졌다. $k_1a_1 + k_2a_2 + \cdots + k_na_n = \vec{0}$의 non-zero solution의 존재 여부를 찾으면 된다! 그건 어떻게 찾냐? 조금 뒤에 알아보자.


# Matrix
$m \times n$ 행렬(matrix)은 $m$개의 row와 $n$개의 column을 가진 rectangular array다. 보통 다음과 같이 표현한다.

$$
A = 
\begin{pmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\cdots&\cdots&\cdots&\cdots\\
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{pmatrix}
$$

캬 쓰기 참 어렵다. 여기서 $i^{th}$ column과 $j^{th}$ column에 해당하는 원소는 $a_{ij}$와 같이 denote한다.

몇 가지 특별한 행렬들에 대해 짚고 넘어가자.

- Square matrix: $m \times m$인 행렬.
- Identity matrix: $a_{ii} = 1$ for all $i$이며, 그 외의 원소는 모두 0인 행렬. Identity matrix는 square matrix고, 사이즈, $n$에 따라 $I_n$으로 표기한다. 
- Zero matrix: $a_{ij} = 0$ for all $i, j$인 행렬, 주로 볼드체로 $\mathbf{0}$으로 표기한다.

## Operations
### Addition & Scalar Multiplication
행렬 또한 벡터처럼 (같은 size의 두 행렬에 대한) addition과 scalar multiplication을 수행할 수 있다. 

방식은 비슷하니 따로 설명은 하지 않고 패스!

### Transpose
전치(transpose), 즉 원소 각각의 행과 열을 반전시키는 연산이다. 가령 $a_{ij}$면 $a_{ji}$에 위치하게 된다. 꼭 정사각행렬(square matrix)일 필요는 없고, 전치 후 $m \times n$ 행렬은 $n \times m$ 행렬이 된다.

$$
A^T = 
\begin{pmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\cdots&\cdots&\cdots&\cdots\\
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{pmatrix}^T =
\begin{pmatrix}
a_{11}&a_{21}&\cdots&a_{n1}\\
a_{12}&a_{22}&\cdots&a_{n2}\\
\cdots&\cdots&\cdots&\cdots\\
a_{1m}&a_{2m}&\cdots&a_{nm}
\end{pmatrix}
$$

여기서, $A^T = A$를 만족하는 행렬을 symmetric matrix라고, $A = -A^T$를 만족하는 행렬을 skew-symmetric matrix라고 한다. 자연스럽게, symmetric하려면 일단 square이고 봐야한다는 사실도 알 수 있다.

## Determinant
행렬식(determinant)이란 정사각행렬이 가지는 행렬의 고유한 값이다. 행렬식을 구하는 방법은 다양하지만, 그나마 편한 방법으로, 정사각행렬 $[A]_{n \times n}$에 대해 다음과 같이 정의한다.

$$ det(A) = \vert A \vert = \begin{vmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&a_{22}&a_{23}\\
a_{31}&a_{32}&a_{33}
\end{vmatrix}  = \sum_{j=1}^n a_{ij} \cdot A_{ij}
$$

$A_{ij}$는 $a_{ij}$의 cofactor라 불리며, $(-1)^{i+j}\vert M_{ij}\vert$와 같이 정의된다. $M_{ij}$는 $a_{ij}$의 minor라 불리며, $A$에서 $i^{th}$ row와 $j^{th}$ column을 제거한 $n-1 \times n-1$ 행렬이다. 예를 들어,

$$ A = \begin{pmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&a_{22}&a_{23}\\
a_{31}&a_{32}&a_{33}
\end{pmatrix}$$

여기서, $a_{11}$의 minor, $M_{11}$는 다음과 같다.

$$ M_{11} = \begin{pmatrix}
a_{22}&a_{23}\\
a_{32}&a_{33}
\end{pmatrix}
$$

이러한 방식으로, (좀 더 간단하게 구할 수 있는) 작은 행렬식을 여러 번 계산하는 것으로 큰 행렬의 행렬식을 구할 수 있다. 어느 정도 recursive한 셈이다. 그런데, 그러면 $1 \times 1$까지 줄여야 하나? 너무 비효율적이고 계산이 너무 많아지는 거 아닌가? 싶은데, 작은 행렬을 구하기 위한 간단한 공식들이 있다.

$$det(A) = \vert a_{11}\vert = a_{11} $$

$$det(A) = \begin{vmatrix} a_{11}&a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}$$

$3 \times 3$행렬도 있지만, 여기서 mathjax로 쓰다가 혈압올라서 그만뒀다. [Arrow Method](https://www.coolmath.com/algebra/14-determinants-cramers-rule/02-determinants-3x3-method-1-01)를 참고하자. 아무튼 $2 \times 2$ 행렬의 경우, 행렬식을 구하기가 상대적으로 쉬우니, 보통 $2 \times 2$까지 분할해서 행렬식을 구한다.

예제로 딱... 딱 하나만 해보자. 아래 행렬식을 계산해보자.

$$
det(A) \;= {\begin{vmatrix} 3 & 2 & 7 \\
            1 & 1 & 3 \\
            5 & 5 & -6
            \end{vmatrix}} \\
\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;{=3 {\begin{vmatrix}
        1&3\\
        5&-6
        \end{vmatrix}}
    -2 {\begin{vmatrix}
        1&3\\
        5&-6
        \end{vmatrix}}
    +7 {\begin{vmatrix}
        1&1\\
        5&5
        \end{vmatrix}}} \\
\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;= -63 + 42 + 0 \\
= -21
$$

왜 align이 안먹히냐... 아무튼 이렇게 구할 수 있다.

## Rank
이제 행렬을 row vector, 혹은 column vector의 집합으로 보자. 결국 벡터도 $n \times 1$, 혹은 $1 \times n$의 행렬로 볼 수 있기 때문에, 그렇게 이상한 일은 아니다.

벡터를 알아보면서, 우리는 벡터들이 선형 독립(LI)일 조건에 대해서도 살펴보았다. Rank는 그 행렬을 구성하는 벡터 집합에서, 선형 독립인 벡터 부분 집합의 **최대** 원소 수를 의미한다. Row vector를 기준으로 하면 row rank, column vector를 기준으로 하면 column rank다.

Rank엔 몇 가지 흥미로운 성질이 있다. 

- Rank, $r(A)$는 반드시 $min \{ m, n \} $보다 작거나 같다. 행렬 사이즈를 초과해서 벡터를 가질 순 없기 때문이다.
- 모든 행렬에 대하여, 한 행렬의 Row rank와 column rank는 항상 같다. (Rank theorem)

그리고 $r(A) = min \{ m, n \} $이면, $r(A)$는 full rank라고 한다.

## Matrix Multiplication
두 행렬 간의 곱셈도 가능한데, 여기엔 조건이 있다.

> $m \times n$ 행렬 $A$와 $x \times y$ 행렬 $B$에 대하여, $n = x$일 때 행렬의 곱이 정의되며, 행렬 곱의 크기는 $m \times y$다.

Vector의 inner product도 비슷한 맥락에서 바라볼 수 있다. Row vector에 column vector를 곱하므로 $(1 \times n) \times (n \times 1)$인 셈이기 때문이다. 그 결과도 $(1 \times 1)$이고.

그래서 행렬 곱은 어떻게 구하냐? 하면 다음과 같이 정의된다.

$A_{m\times n}B_{n\times l} = [c_{ij}]_{m \times l}$

여기서 $c_{ij}$는 $A$의 $i^{th}$ row, $B$의 $j^{th}$ column의 inner product다. 즉, inner product를 $m \times l$번 해서 $m \times l$ 사이즈의 행렬을 얻는다.

예시는 풀지 않는다. 쓰다가 늙어 죽을지도 몰라...

행렬 곱을 알았으니, identity matrix를 다시 살펴보자. Identity matrix는 다음과 같은 성질을 만족한다. 크기가 맞는 행렬 $A$에 대하여,

- $AI = IA = A$

또, 행렬곱은 일반적으로 결합법칙은 성립하나 교환법칙이 성립하지 않는다. 뒤에서 볼 역행렬과 단위행렬이 조금 특이한 케이스다.

## Inverse Matrix & Singularity
어떤 행렬 $A$에 대한 행렬곱, $AB = BA = I$를 만족하도록 하는 행렬 $B$를 $A$의 역행렬(inverse matrix)이라 한다.

역행렬도 존재하기 위한 조건이 있다. 기본적으로 역행렬이 존재하는 행렬은 정사각행렬이다. 왜냐? (marginal 하니 넘어가려면 넘어가자)

> 우선, 행렬 $A$가 $m \times n$이라면, $AB$가 정의되기 위해 B는 $n \times l$의 크기를 가져야 하는데, 결과가 identity matrix이므로, (정사각이기 때문에) $m = l$이어야 한다. 그리고 $BA$도 정의되어야 하고, 그 결과에 의한 identity의 사이즈도 $AB$의 것과 같아야 하므로, $m=l=n$이다. 즉, $A$는 정사각행렬이다.

정사각행렬이라고 반드시 역행렬이 있는 건 아님에 주의하자. 아무튼 정사각행렬임이 보장되었으니, 행렬식도 구할 수 있을 것이다. 다음 두 statement는 서로 동치다.

- $det(A) \ne 0$ (non-singular)
- $A$ has its own inverse matrix, $A^{-1}$

이 때, $det(A)$가 $0$일 때, 그 행렬은 singular하다고 하며, 그렇지 않으면 non-singular하다고 한다. 즉, 행렬식을 구해보면 역행렬의 존재성을 할 수 있다는 사실!

역행렬을 구하는 건 어떻게 할까? 많은 방법이 있지만, 가장 쉬운 방법은 인터넷에 떠돌아다니는 행렬 계산기를 쓰는 거다. 그래서 나도 내 손으로 역행렬을 구한 지 몇 년이 되었는데, 아무튼 주로 두 방법을 쓰니 알아서 살펴보자. 차마 내 손으론 못쓰겠다...

- [Cramer's Rule](https://en.wikipedia.org/wiki/Cramer%27s_rule)
- [Gauss-Jordan Elimination](https://www.mathsisfun.com/algebra/matrix-inverse-row-operations-gauss-jordan.html)

## Elementary Row Operation
Elementary row operation은 행(row) 단위로 수행할 수 있는 연산을 의미한다. 이게 왜 중요하냐? 하면, 이 연산들은 수행해도 행렬이 가지는 주요 성질들을 변화시키지 않기 때문이다. 행렬식, 역행렬의 존재성, rank 등 많은 것을 보존하는 연산이다. 또, 이는 상당히 유용한데, 성질을 보존하므로 우리가 계산하기 쉬운 형태로 행렬을 변형할 기회를 주기 때문이다.

- $kR_i \to R_i$: $i^{th}$ row에 scalar $k$를 곱한다.
- $R_i + R_j \to R_{i}$: 다른 row에 어떤 row를 더한다.
- $R_i + kR_j \to R_{i}$: 다른 row에 어떤 row의 scalar multiplication을 더한다.

Gauss-Jordan Elimination도 elementary row operation을 사용하고, 후에 언급할 RREF도 이걸로 구하고, 정말 쓸 곳이 많은 연산이다.

또, 이렇게 $A$에 elementary row operation을 통해 $B$를 얻을 수 있다면, 그 둘은 row-equivalent하다고 한다. 이 연산이 많은 성질을 보존하므로, row-equivalent하면 그 성질들 또한 공유한다고 볼 수 있다.

## Equivalence Theorem
임의의 정사각($n \times n$) 행렬 $A$에 대하여, $A$는 다음과 같은 성질은 모두 만족하거나, 모두 만족하지 않는다. 다 볼 필요는 없다. 수 십 개의 동치 명제들이 있는데, 몇 개만 가져와봤다.

- $det(A) \ne 0$
- $Ax = 0$에서 $x$는 반드시 trivial solution($x = \vec 0$)만을 가진다.
- $A$의 역행렬이 존재한다. (invertible)
- $r(A) = n$
- 모든 linear system $Ax=b$에 대해, $x$는 unique solution을 가진다.
- A는 $I_n$과 row-equivalent하다.

다시 말하면, 행렬식 하나만 구해도 그 행렬의 많은 걸 알 수 있다. 그런데 singular하면 그건 또 그것대로 골때리게 되는 셈이지.


# Solving Linear Systems
정말 힘든 시간이었다. 이제 배경지식을 쌓았으니 linear system을 풀어보자!

다음과 같은 simultaneous linear equation을 푼다고 가정하자.

$$
\begin{matrix}
a_{11}x_1 + a_{12}x_2 + \cdots a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots a_{2n}x_n = b_2 \\
\cdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots a_{mn}x_n = b_m
\end{matrix}
$$

이를 행렬 형태로 변환하여, 다음과 같이 나타낼 수 있다.

$$
\mathbf{Ax}=
\begin{pmatrix}
a_{11}&a_{21}&\cdots&a_{n1}\\
a_{12}&a_{22}&\cdots&a_{n2}\\
\cdots&\cdots&\cdots&\cdots\\
a_{1m}&a_{2m}&\cdots&a_{nm}
\end{pmatrix}
\begin{pmatrix}
x_1\\x_2\\ \cdots \\ x_n
\end{pmatrix} =
\begin{pmatrix}
b_1\\b_2\\ \cdots \\ b_m
\end{pmatrix} = \mathbf b
$$

왜냐? 행렬곱을 해보면 똑같이 나온다... 이게 더 이쁘기도 하고.

## Existence of Solution
주어진 linear system의 해의 존재성을 파악하기 위한 여러 방법이 있다.

우선 rank를 이용해보자. $m \times n$ 행렬 $\mathbf A$와 $\mathbf A$, $\mathbf b$를 붙여 만든 augmented matrix $\mathbf A \vert \; \mathbf b$에 대해, 각각의 rank를 계산한다.

- $r(A) = r(A \vert\; b) = n$: Linear system은 consistent하고, unique solution을 가진다.
- $r(A) = r(A \vert\; b) < n$: Linear system은 consistent하고, infinite solution을 가진다.
- $r(A) < r(A \vert\; b) = r(A) + 1$: Linear system은 inconsistent하고, solution을 가지지 않는다.

결국, $\mathbf b$가 $A$의 column vector 간의 linear combination으로 만들어질 수 있다면 해가 존재하는 셈이다. (역도 성립한다.)

더 간단한 방법으로, (정사각행렬의 경우) 위에서 언급한 동치 명제들을 이용할 수도 있다.

- $det(A) \ne 0$
- $Ax = 0$에서 $x$는 반드시 trivial solution($x = \vec 0$)만을 가진다.
- $A$의 역행렬이 존재한다. (invertible)
- $r(A) = n$
- 모든 linear system $Ax=b$에 대해, $x$는 unique solution을 가진다.
- A는 $I_n$과 row-equivalent하다.

간단히 행렬식만 확인하면 된다. 와!

## Solution
### Unique Solution
$\mathbf {Ax = b}$가 unique solution을 가지고 (non-singular), A는 정사각행렬인 경우를 알아보자. 아이디어는 간단하다. $\mathbf {Ax=b}$라면, $\mathbf{A^{-1}(Ax) = A^{-1}b}$고 (non-singular이므로 역행렬이 반드시 존재한다.) 이 식을 교환법칙을 이용해 정리하면, $\mathbf {(A^{-1}A)x = Ix=x=A^{-1}b}$다. 즉, 역행렬을 구하고, 거기다 $\mathbf {b}$를 곱하면 된다.

역행렬은 알아서 구하면 되는데, Gauss-Jordan Elimination을 추천하고, 난 행렬 계산기를 사용할 예정이다.

### Infinite Solution
$\mathbf {A}$가 역행렬을 가지지 않는다면 참 난감하다. $det(A) = 0$이어서 가지지 않을 수도(singular), 아니면 정사각행렬이 아니어서(non-square) 가지지 않을 수도 있다. 이번엔 $r(A) = k < n$이어서 infinite solution인 경우를 알아보자. 우리는 이 system에서 general solution을 찾는 게 목표다.

가장 간단한 방법으로, 주어진 $\mathbf {A, b}$에 대한 augmented matrix, $\mathbf {A \vert\; b}$의 RREF(Reduced Row Echelon Form)를 만드는 것으로 해결해보자.

#### RREF
RREF는 다음을 조건을 만족하는 행렬 형태다.

1. 각 row에 대해, 가장 먼저 나타나는 non-zero element는 반드시 1이다. 이를 pivot이라고 하자.
2. 어떤 $i^{th}$ row에 pivot이 있었다면, $j^{th} (> i)$ row는 (만약 존재한다면) 반드시 $i^{th}$ row의 pivot보다 오른쪽에 위치한다.
3. Pivot이 없는 row는 zero-row-vector고, 이는 반드시 pivot이 있는 row의 아래에 위치한다.
4. Pivot을 포함하는 column에서, pivot을 제외한 모든 원소는 0이다.

1, 2, 3, 4번을 모두 만족하면 RREF, 1, 2, 3번을 만족하면 REF(Row Echelon Form)이라고 한다. 주어진 행렬에 대하여 RREF는 유일하나, REF는 그렇지 않다. 몇 가지 예시를 들어보자.

$$\begin{pmatrix}
1&2&3&4\\
0&0&1&2\\
0&0&0&0
\end{pmatrix}
$$

위 행렬은 REF이나, RREF는 아니다. 두 번째 row의 pivot이 있는 column에 pivot 외의 non-zero element가 있기 때문이다.

$$\begin{pmatrix}
1&2&0&4\\
0&0&1&2\\
0&0&0&0
\end{pmatrix}
$$

반면, 위 행렬은 RREF다.

#### Getting General Solution by RREF
다시 원점으로 돌아와, 우리는  $\mathbf {A \vert\; b}$의 RREF를 만드는 것으로 해결한다고 했다. 왜냐? RREF로 만들면 해가 명확하게 드러나기 때문이다. 예를 들어, 다음과 같이 RREF로 만든 linear system을 생각해보자.


$$\begin{pmatrix}
1&0&2&0 &\vert\; 13\\
0&1&1&0&\vert \; 25\\
0&0&0&1 &\vert \; 18\\
\end{pmatrix}
$$

솔루션이 꽤 명확히 보인다. Pivot을 기준으로 식을 정리하면 된다.

$$\begin{pmatrix}
x_1\\x_2\\x_3\\x_4
\end{pmatrix}=
\begin{pmatrix}
13-2x_3\\25-x_3\\x_3\\18
\end{pmatrix}
$$

여기서 $x_3$이 흥미로운데, 이를 free variable로 여겨, 다른 변수가 그것에 관한 식으로 해를 구성할 수 있도록 할 수 있다. 즉, $x_3 = t$로 놓으면,

$$\begin{pmatrix}
x_1\\x_2\\x_3\\x_4
\end{pmatrix}=
\begin{pmatrix}
13-2t\\25-t\\t\\18
\end{pmatrix}=
\begin{pmatrix}
13\\25\\0\\18
\end{pmatrix}+t
\begin{pmatrix}
-2\\-1\\1\\0
\end{pmatrix}
$$

이렇게 general solution을 구할 수 있게 되었다!! 여기서 free variable을 0으로 놓고 나온 solution, $(13, 25, 0, 18)^T$를 basic solution, $x_B$라 하고, free variable이 아닌 변수들을 basic variable이라 하자. 또, free variable이 구성하는 벡터를 $x_N$과 같이 나타낼 것이다.

$$x_B = \begin{pmatrix}
13\\25\\0\\18
\end{pmatrix}, x_N=
\begin{pmatrix}
x_3
\end{pmatrix}$$

### Infeasible Solution
이 또한 RREF로 간단히 확인할 수 있다. 위와 같은 방식으로 RREF를 만들었는데, $\mathbf A$의 row vector가 zero vector인데, 그 행의 $\mathbf b$ 원소가 non-zero다? 그러면 우리는 해가 없다고 결론 지을 수 있다. 다음과 같은 상황이다.

$$\begin{pmatrix}
1&0&2&3 &\vert\; 2\\
0&1&2&6&\vert \; 1\\
0&0&0&0 &\vert \; 1\\
\end{pmatrix}
$$

$0x_1 + 0x_2+0x_3+0x_4 = 1 $의 해를 찾는 것과 같은 일이다. 당연하게도 해가 있을 수 없다.


# 마치며
결국 행렬 계산기를 쓰는 게 정신 건강에 이롭다. 이론적 배경과 솔루션을 구하는 과정만 잘 숙지해놓고, 계산기를 열심히 쓰자.