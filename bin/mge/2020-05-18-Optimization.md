---
title: "Optimization"
tags: Management-Engineering
toc: true
---

# Operations Research
__운용과학(operation research, OR)__ 이란, 주어진 문제 상황이나 시스템에 대해, 수학적/통계적 모델의 적용을 통해 합리적인 의사 결정을 이끌어내는 방법을 의미한다. OR을 위해 우리는 다양한 방법들을 사용할 수 있는데, 최적화, 데이터 분석, 시뮬레이션 등이 그 예시다. 이들은 주어진 문제와 시스템을 수학적으로 모델링하는 데 사용될 수 있다.

![](/imgs/mge/mge1.png)

OR이 커버하는 범위는 광범위하다. 일반적인 비즈니스 모델부터, 각종 공학, 군사 및 정책적인 분야에서도 활용될 수 있다. 그 시작 또한 WWII에서 군수 물자 보급의 최적화를 위한 시도에서 나왔다고 할 정도니 말이다.

OR에서 사용될 수 있는 모델을 크게 두 가지로 나누어 볼 수 있다.

- Deterministic model: output은 초기 상태(initial condition)와 주어진 파라미터(parameter)에 의해 완전히 결정된다.
- Stochastic model: output은 무작위성(randomness)과 불확실성(uncertainty)을 어느 정도 내포한다. 

Deterministic model이 사용되는 문제에선 optimization을, stochastic model이 사용되는 문제에선 characterization / estimation이 사용된다.

![](/imgs/mge/mge2.png)

그래서 이제부터 우린 여기서 optimization을 위한 여러 기법을 알아보려고 한다.

# Linear Programming
__선형 계획법(linear programming)__ 이란, 선형적 성질을 만족시키는 어떤 목적함수의 최적화를 위한 방법이다. 당연히 우리는 선형적인 함수와 그렇지 않은 함수를 잘 구분할 수 있을 테니, 선형적임이 무엇을 의미하는지는 생략하자.

LP가 사용되는 가장 친숙한 예시는 아마 고등학교 때 배운 부등식의 영역일 것이다. 대개 $k = x + 2y$ 등으로 나타내어 k를 최소화, 혹은 최대화하도록 하는 $x$와 $y$를 찾는 문제가 많이 나왔다. 또, 이런 문제들은 대개 실생활 예시와 엮어 나오는 경우가 많았어서 더욱 친숙할 것이다.

예시를 통해 자세히 알아보겠지만, 일반적인 LP의 절차는 다음과 같다.

1. Decision variable(주로 x)을 결정 및 정의한다. 이는 우리가 결정 및 조작해야 할 변수를 의미한다. 
2. 목적 함수(objective function)를 정의하고 수식으로 표현한다. 목적 함수는 우리가 최적화하려는 대상이다.
3. 제한 요인(constraint)를 정의 및 표현한다. 한정된 자원, 시간 등이 여기에 포함될 것이다.

## Input-Output Problem
여러 종류의 제품 생산 시, 주어진 자원으로 최대 이익을 얻기 위해 어느 제품을 얼마나 만들어야 할까? 이를 LP로 해결할 것이다. 

Notation | Meaning
---|---
$m$ | number of inputs(resources)
$n$ | number of outputs(products)
$A_{ij}$ | output, j를 만들기 위해 필요한 input, i의 양
$b_i$ | 사용 가능한 input, i의 양
$c_j$ | output, j 하나 당 이익(profit)
$x_j$ | 만들어지는 output, j의 양

각각의 input, $i$는 $b_i$만큼만 사용할 수 있으므로, 다음과 같이 나타낼 수 있다.

$A_{11}x_1 + A_{12}x_2 + ... + A_{1n}x_n \le b_1$

$A_{21}x_1 + A_{22}x_2 + ... + A_{2n}x_n \le b_2$

...

$A_{m1}x_1 + A_{m2}x_2 + ... + A_{mn}x_n \le b_m$

그리고 모든 $j$에 대하여, $x_j \ge 0$이다.

여기서 우리는 $z = c_1x_1 + c_2x_2 + ... + c_nx_n$을 maximize하는 게 목표다. 조금 더 깔끔하게 vector-matrix formulation으로 나타낼 수도 있다.

![](/imgs/mge/mge3.png)

뭐 푸는 건 알아서 하자.

## Product-Mix Problem
어떤 자원이 여러 제품을 생산하는 데 사용될 수 있다. 그리고 제한된 자원이라면 이들 사이의 경쟁이 발생할 수 있는데, 그러한 constraint가 주어진 상황에서, 우린 어떻게 최적의 해를 찾을까? 예시를 통해 알아보자.

> 제품 A 생산 시 20달러, B 생산 시 30달러를 벌 수 있다. A와 B 모두 두 개의 공정으로 이루어져 있으며, 이를 공유하므로 A와 B를 동시에 만들 수는 없다. 회사 사정 상, A는 최소 25개 이상 생산되어야 하며, 각 공정에서 A와 B를 만들기 위해 필요한 시간은 다음과 같다.

Step | A | B | Hours available
---|---|---|---
Step 1 | 4 | 3 | 240
Step 2 | 1 | 2 | 140

고등학교 수학 책에서 봤을 법한 문제다. A의 생산량을 $x_1$, B의 생산량을 $x_2$라 하자. 목적 함수는 $z = 20x_1 + 30x_2$고, 제한 요인은 다음과 같다.

- $4x_1 + 3x_2 \le 240$
- $x_1 + 2x_2 \le 140$
- $x_1 \ge 25$
- $x_1, x_2 \ge 0$

## Graphical Solution for LP
부등식의 영역 문제를 풀 때를 기억해보자. 주어진 부등식으로 영역을 표기하여, 목적 함수에 해당하는 그래프가 그 위에 있으면서도 최댓값을 갖도록 몇 개의 특징적인 점들을 검사해보았을 것이다. 그 때는 x, y, 두 변수만을 사용했지만, 우리는 이를 더욱 확장해볼 것이다.

__하이퍼플레인(hyperplane)__ 은 어떤 노멀(normal) 벡터를 기준으로, 그 벡터의 종점을 시점으로 하면서 노멀 벡터에 대해 orthogonal한 벡터의 종점이 이루는 집합이다. 이는 달리 말하면, 노멀 벡터와 임의의 위치 벡터의 내적이 일정한 값을 가지게 하는($px = k$) 점들의 집합으로 볼 수도 있다. 노멀 벡터로 직선 혹은 평면을 결정할 수 있는 사실을 생각하면 쉽다. 단지 그것을 n-dimension으로 일반화시켰을 뿐이다. 아무튼 제대로 정의해보자.

![](/imgs/mge/mge5.png)

![](/imgs/mge/mge4.png)

$E^3$에서의 하이퍼플레인은 일반적인 평면이다.

__하프 스페이스(half-space)__ 는 하이퍼플레인에 의해 나누어진 두 공간 각각을 의미한다. 평면 위 직선이 자기보다 작은 영역과 큰 영역(엄밀하진 않은 워딩이지만)으로 두 공간을 나누듯이 말이다.

![](/imgs/mge/mge6.png)

이러한 방식을 이용해, LP에서 가능한 솔루션들은 제한 요인과 목적 함수에 의해 만들어지는 하프 스페이스와 하이퍼플레인의 교집합으로 표현될 수 있다. 이렇게 (최적 여부에 상관없이) 해가 될 수 있는 영역을 feasible region이라고 한다.

![](/imgs/mge/mge8.png)

우리는 여기서 몇 개의 extreme point를 찾을 수 있다. 위의 예시에선 $(0, 0), (0, 3), (3, 2), (4, 0)$이 있겠다. 가능한 x의 영역은 이 점(에 해당하는 벡터)의 linear combination으로 만들 수 있다.

![](/imgs/mge/mge7.png)

이러한 상황에서, 가능한 경우는 네 가지 정도로 나누어볼 수 있다.

- Unique optimal solution : 해는 유일하게 결정된다.
- Alternative optimal solution : 해는 둘 이상이고, 무수히 많을 수도 있다.
- Unbounded solution : 목적 함수가 발산한다.
- Infeasible : 해가 존재하지 않는다.


# Convex Optimization
앞에선 주어진 조건(제한 요인)과 목적 함수가 선형적임을 가정했다. 이번엔, 이들이 convex function인 경우의 최적화를 알아보도록 하자.

## Convexity 
우선 convex하단 게 어떤 건지 명확히 짚고 넘어가야 한다. __Convex combination__ 이란, 두 점 $x_1, x_2$를 잇는, 다음과 같은 성질을 만족하는 점들의 집합, $L$이다.

$$ L(x_1, x_2) = \{y : y \alpha x_1 + (1-\alpha)x_2 \} $$

$\alpha$는 0과 1 사이의 값이다. 즉, 간단히 말해 두 점을 잇는 선을 멋지게 정의한 셈이다.

![](/imgs/mge/mge9.png)

그리고 __convex set__ 이란, 집합 내의 임의의 점 $x_1, x_2$에 대해, 그것의 convex combination 또한 집합에 포함되어 있도록 하는 집합 $S$를 의미한다. 

![](/imgs/mge/mge11.png)

Convex combination은 아마 그 자체로 convex set일 것이다. 그리고 토러스 형태의 입체는 convex set이 아닐 것이다. 집합이 visualize되어 있다면 쉽게 확인할 수 있는 사항이다.

![](/imgs/mge/mge10.png)

Convex combination은 다수의 점에 대해서도 정의할 수 있다. 우린 아까 이걸 자연스럽게 썼었는데, extreme point에 해당하는 벡터로 영역 내의 점들의 집합을 표현했을 때 그 개념을 사용했다.

![](/imgs/mge/mge12.png)

아니, 그런데 extreme point가 뭔지는 정의했었나? 확실히 짚고 넘어가자. __Extreme point(EP)__ 란 strict convex combination으로 나타내어지지 않는 점을 의미한다. 여기서 strict하단 말은, $\alpha$가 1이나 0이 아니라는 의미다. 

![](/imgs/mge/mge13.png)

정의 몇 가지만 더 하고가자. 수학 과목을 하는 기분이다.

- 어떤 방향 단위벡터 $d$에 대해, 모든 non-zero 벡터 $x$와 모든 스칼라 상수 $\lambda$에 대해 $x+\lambda d \in S$면 $S$는 그 방향에 대해 unbound다.
- 어떤 집합이 unbound여서, $R= \{x+\lambda d \in S : \lambda \ge 0 \}$ 내의 점이 모두 집합에 포함될 때, $R$을 ray라고 한다.
- 집합 내에서 어떤 방향벡터 $d$가 다른 방향벡터 둘의 positive-linear-combination으로 나타내어지지 않는 경우, 이를 extreme direction(ED)이라고 한다.
- EP와 ED에 의해 만들어지는 직선, $R= \{x+\lambda d \in S : \lambda \ge 0 \}$을 extreme ray라고 한다.

왜 이런 짓을 하고 있는지 의문이 들 것이다. 사실 나도 그렇다. 이후에 사용할 optimization에 사용될 수학적 베이스가 되겠지 하고 넘기고 있다. 아무튼 이제 convex/concave function을 잘 정의할 수 있게 되었다.

![](/imgs/mge/mge14.png)

아하! 주어진 $\alpha$에 대해, 두 함숫값, $f(x_1), f(x_2)$의 convex combination이 $x_1$과 $x_2$의 convex combination에서의 함숫값보다 작거나 같으면 된다! 실제로 이렇게 정의하면 우리가 일반적으로 알고 있는 convexity와 잘 통한다.

![](/imgs/mge/mge15.png)

반대로 concave는 함숫값의 convex combination이 크거나 같으면 될 것이다. 그렇다면 linear function이면 convex하면서 동시에 concave할까? 그렇다! Convex하지 않다고 반드시 concave하진 않은 셈이다.

또, 이 모든 것은 convex set 안에서 일어남을 알아두자. 도넛 형태 평면 위의 점들을 변수로 가지는 함수라면 convex/concave가 잘 판단될 수 있을까? 물론, convex set 위에서도 convex하지 않으면서 concave하지도 않은 경우가 있다. 꼬불꼬불거리는(?) 함수가 그 예시다. 물론 일부를 따면 convex한 부분과 concave한 부분이 있겠지만, 그 함수 자체는 아니니.





