---
title: "Convexity"
tags: OR Management-Engineering
toc: true
---

# Intro
이번엔 **convexity**에 대한 개념과 관련된 정의들, 그리고 그로부터 파생되는 많은 성질과 정리들을 알아볼 예정이다.

# Definitions
항상 정의를 명확히 아는 게 중요하다! 이번엔 여러 개념들의 정의를 각각 알아보고, 사이드로 그 개념들에 대한 여러 성질을 소개할 것이다.

## Line segment
어떤 두 $x_1, x_2 \in E^n$에 대하여, 다음을 만족하는 집합을 **line segment**라 하자.

$L(x_1, x_2) = $ {$y: y=\alpha x_1 + (1-\alpha)x_2$} where $0\le\alpha\le 1$
{:.success}

위와 같은 정의는 우리가 일반적으로 생각하는 라인 세그먼트와 그 의미가 딱 들어맞는다. 라인 세그먼트를 두 점을 잇는 선 위의 점들의 집합으로 보면 직관적으로 이해할 수 있을 것이다.


## Convex Set
어떤 집합 $S \subset E^n$은 다음과 같은 조건을 만족할 때 **convex set**이라고 부를 수 있다.

For any $x_1, x_2 \in E^n$, $L(x_1, x_2) \subseteq S $
{:.success}

그럼 어떤 집합이 convex하고, 어떤 집합이 convex하지 않을까? 예시를 조금 살펴보자.

![](/imgs/mge/or1.png)

위와 같은 집합은 convex set이다. 집합 내의 어느 두 점을 잡아도, 그 둘에 대한 라인 세그먼트는 항상 원래 집합의 부분집합이다.

![](/imgs/mge/or2.png)

반면, 위와 같은 집합은 non-convex set이다. 그림과 같은 예시에서 라인 세그먼트의 일부가 집합에 포함되지 않기 때문이다.


## Convex Combination
어떤 벡터, $x_1, x_2, \cdots, x_k \in E^n $에 대해, 다음과 같은 벡터 연산을 생각할 수 있다.

$\mathbf x= \alpha_1x_1 +\alpha_2x_2 + \cdots + \alpha_kx_k$ where $\alpha_i \ge 0 $ for $i=1,2,\cdots,k$ and $\alpha_1 + \alpha_2 + \cdots + \alpha_k = 1$
{:.success}

다음과 같은 $\mathbf x$를 $x_1, x_2, \cdots, x_k$에 대한 **convex combination**이라고 부르자. 또, $ 0< \alpha < 1$, 즉, 등호를 허용하지 않는 convex combination은 **strict convex combination**이라고 부른다.

![](/imgs/mge/or3.png)

위의 예시를 보자. 세 벡터에 의해 만들어지는 (경계와 내부를 모두 포함한) 저 공간이 세 벡터에 대한 convex combination으로 표현 가능한 영역이다.

위 그림을 보면, 다음과 같은 생각을 해볼 수 있다.

> 그럼 주어진 벡터에 대한 convex combination들의 집합도 convex set일까?

결론부터 말하면 그렇다! 증명은 쉬우니까 생략한다. 

## Extreme Point
어떤 convex set, $S \subset E^n$에 대해, **extreme point(EP)**는 다음 조건을 만족하는 포인트, $\mathbf x$를 의미한다.

$\mathbf x$는 다른 두 포인트, $x_1, x_2 \in S$의 strict convex combination으로 표현될 수 없다.
{:.success}

![](/imgs/mge/or3.png)

위의 예시를 다시 가져와봤다. $x_1$ 은 $\alpha x_1 + (1-\alpha)x_1 = x_1$로만 표현될 수 있고, 다른 포인트 또한 그렇다. 즉, $x_1, x_2, x_3$은 모두 EP라고 할 수 있겠다. 반면, 이 세 점을 제외한 경계나 내부는 모두 EP가 아니다.

EP가 무수히 많은 경우도 있다.

![](/imgs/mge/or4.png)

## Adjacency
우리는 두 EP에 대해, 인접한지 아닌지에 대한 여부를 직관적으로 판단할 수 있다. 가령 직사각형 모양 집합에서 대각선 방향으로 서로 바라보는 두 점은 인접하지 않을 것이다. 위의 삼각형 모양 예시에선 모든 EP가 서로 인접할 것이고.

하지만 우리는 이 인접하다는 표현을 조금 더 명확히 하고 싶다. 이제부터 두 EP에 대한 라인 세그먼트가 해당 convex set의 모서리(edge)를 형성할 때, 두 EP가 **인접(adjacent)** 하다고 부르자.

상상 속에서 어떤 convex set과 그것의 EP들을 생각해보자. 직관과 딱 들어맞는 정의라고 할 수 있다!

## Hyperplane
어떤 non-zero 벡터 $p \in E$에 대해, **hyperplane**, $H$는 다음과 같이 정의된다.

$H = $ {$x: x \in E^n, p\cdot x = k$}, where $k \in E$
{:.success}

즉, $p$와 $x$의 inner product가 상수가 되도록 하는 $x$의 집합이다. 

## Half-Space
주어진 hyperspace에 대하여, 우리는 $E^n$을 두 공간으로 이분할 수 있다.

- $H^- = $ ${x: x\in E^n, p\cdot x \le k}$
- $H^+ = $ ${x: x\in E^n, p\cdot x \ge k}$

이들 각각을 **half-space**라고 하며, 이들은 convex set이다.

## Unboundedness, Extreme Direction
어떤 convex set은 유계가 아닐 수도 있다. 다음 조건을 만족할 때 우리는 집합 $S$를 **unbounded set**이라고 부른다.

모든 $x \in S$와 scalar, $\lambda \ge 0$에 대해, $x + \lambda d \in S$인 $d$가 있다면 그 집합은 unbound하다. 
{:.success}

![](/imgs/mge/or5.png)

그리고 이러한 direction 중, 서로 다른 두 direction의 positive linear combination으로 표현되지 않는 것을 **extreme direction(ED)** 라고 한다.

또, 어떤 EP, $x$와 ED, $d$에 대한 다음과 같은 집합을 $S$에서의 $x$, $d$에 대한 **extreme ray**라고 한다.

$R = $ {$x + \lambda d \in S, \lambda \ge 0$}
{:.success}

## Convex Cone
다음과 같은 convex set, $C$를 **convex cone**이라고 부르자.

$x \in C \implies \alpha x \in C$ for all $\alpha \ge 0$
{:.success}

그 정의에 의해, convex cone은 반드시 원점을 포함하고($\alpha =0$), 원점을 vertex로 하는 ray가 최소 하나 이상 존재한다.

## Convex / Concave Functions
이제 함수의 convexity와 concavity를 확인해보자. 어떤 convex set, $S \subset E^n$과 $f(x)\;(for\;x \in S)$에 대해, **Convex function**과 **concave function**은 각각 다음과 같은 성질을 만족하는 함수를 의미한다.

- Convex: $f(\alpha x_1 + (1-\alpha)x_2) \le \alpha f(x_1) + (1-\alpha)f(x_2)$ for $x_1, x_2 \in S$ and $0 \le \alpha \le 1$
- Concave: $f(\alpha x_1 + (1-\alpha)x_2) \ge \alpha f(x_1) + (1-\alpha)f(x_2)$ for $x_1, x_2 \in S$ and $0 \le \alpha \le 1$

즉, 어떤 두 점 $x_1, x_2$과 적당한 $\alpha$를 잡아, $(x, f(x))$가 형성하는 라인 세그먼트를 기준으로, 두 점의 convex combination의 함숫값이 위에 있는지, 아래에 있는지를 기준으로 convexity / concavity를 판단할 수 있다. 

또, 정의에 의하여, 선형 함수는 convex하면서 concave한 함수다.

## Polyhedral Set / Cone
유한한 half-space 간의 교집합(intersection)을 **polyhedral set**이라고 한다. 즉,

$S =  \bigcap_{i} $ {$x \in E^n: a_ix \le b_i$}
{:.success}

![](/imgs/mge/or6.png)

그리고 그 중에서도 모든 hyperplane이 원점을 지나는 경우를 **polyhedral cone**이라고 한다.

![](/imgs/mge/or7.png)

### Representation Theorem
Polyhedral set에 대한 괜찮은 정리가 하나 있다.

어떤 집합 $S$가 non-empty, bounded인 polyhedral set이라면, **$S$의 모든 EP는 유한하면서 non-empty**고, (1) **모든 $x \in S$는 EP의 convex combination으로 표현될 수 있다**. (2)
{:.success}

사실 이것은 우리가 bounded한 LP를 풀었을 때 자연스럽게 사용했던 정리다.  


# 마치며
사실 다 어느 정도 그 의미를 알고 있는 개념들이지만, 수학적으로 조금 더 명확하게 정의하고 의미를 알아보았다. 다음에는 **simplex method**로 LP를 해결하는 방법을 알아보도록 하자.