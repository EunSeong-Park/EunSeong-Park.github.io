---
title: "Intro to Linear Algebra"
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

- $A = (a_{11})$의 행렬식은 $a_{11}$이다.
- $A = \begin{pmatrix} a_{11}&a_{12}\\a_{21}&a_{22} \end{pmatrix}$의 행렬식은 $a_{11}a_{22} - a_{12}a_{21}$이다. 대각선 방향으로 원소를 곱해 빼준다고 생각하면 된다.

$3 \times 3$행렬도 있지만, 여기서 mathjax로 쓰다가 혈압올라서 그만뒀다. [Arrow Method](https://www.coolmath.com/algebra/14-determinants-cramers-rule/02-determinants-3x3-method-1-01)를 참고하자. 아무튼 $2 \times 2$ 행렬의 경우, 행렬식을 구하기가 상대적으로 쉬우니, 보통 $2 \times 2$까지 분할해서 행렬식을 구한다.

예제로 딱... 딱 하나만 해보자. 아래 행렬식을 계산해보자.
$ det(A) = \begin{vmatrix} 3 & 2 & 7 \\
1 & 1 & 3 \\
5 & 5 & -6
\end{vmatrix}$

$= 3\begin{vmatrix}
1&3\\
5&6
\end{vmatrix} -2\begin{vmatrix}
1&3\\
5&-6
\end{vmatrix} + 7\begin{vmatrix}
1&1\\
5&5
\end{vmatrix}$
$
= -27 + 42 + 0 = -15
$
