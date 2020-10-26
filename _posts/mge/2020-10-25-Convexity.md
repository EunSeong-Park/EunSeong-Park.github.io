---
title: "Convexity"
tags: OR Management-Engineering
toc: true
---

# Intro
이번엔 **convexity**에 대한 개념과 관련된 정의들, 그리고 그로부터 파생되는 많은 성질과 정리들을 알아볼 예정이다.

# Definitions
항상 정의를 명확히 아는 게 중요하다!

## Line segment
어떤 두 $x_1, x_2 \in E^n$에 대하여, 다음을 만족하는 집합을 **line segment**라 하자.

> $L(x_1, x_2) = $ {$y: y=\alpha x_1 + (1-\alpha)x_2$} where $0\le\alpha\le 1$

위와 같은 정의는 우리가 일반적으로 생각하는 라인 세그먼트와 그 의미가 딱 들어맞는다. 라인 세그먼트를 두 점을 잇는 선 위의 점들의 집합으로 보면 직관적으로 이해할 수 있을 것이다.


## Convex Set
어떤 집합 $S \subset E^n$은 다음과 같은 조건을 만족할 때 **convex set**이라고 부를 수 있다.

> For any $x_1, x_2 \in E^n$, $L(x_1, x_2) \subseteq S $

그럼 어떤 집합이 convex하고, 어떤 집합이 convex하지 않을까? 예시를 조금 살펴보자.

![](/imgs/mge/or1.png)

위와 같은 집합은 convex set이다. 집합 내의 어느 두 점을 잡아도, 그 둘에 대한 라인 세그먼트는 항상 원래 집합의 부분집합이다.

![](/imgs/mge/or2.png)

반면, 위와 같은 집합은 non-convex set이다. 그림과 같은 예시에서 라인 세그먼트의 일부가 집합에 포함되지 않기 때문이다.


## Convex Combination
어떤 벡터, $x_1, x_2, \cdots, x_k \in E^n $에 대해, 다음과 같은 벡터 연산을 생각할 수 있다.

> $\mathbf x= \alpha_1x_1 +\alpha_2x_2 + \cdots + \alpha_kx_k$ where $\alpha_i \ge 0 $ for $i=1,2,\cdots,k$ and $\alpha_1 + \alpha_2 + \cdots + \alpha_k = 1$

다음과 같은 $\mathbf x$를 $x_1, x_2, \cdots, x_k$에 대한 **convex combination**이라고 부르자. 또, $ 0< \alpha < 1$, 즉, 등호를 허용하지 않는 convex combination은 **strict convex combination**이라고 부른다.

![](/imgs/mge/or3.png)

위의 예시를 보자. 세 벡터에 의해 만들어지는 (경계와 내부를 모두 포함한) 저 공간이 세 벡터에 대한 convex combination으로 표현 가능한 영역이다.

위 그림을 보면, 다음과 같은 생각을 해볼 수 있다.

> 그럼 주어진 벡터에 대한 convex combination들의 집합도 convex set일까?

결론부터 말하면 그렇다! 증명은 쉬우니까 생략한다. 

## Extreme Point
어떤 convex set, $S \subset E^n$에 대해, **extreme point(EP)**는 다음 조건을 만족하는 포인트, $\mathbf x$를 의미한다.

> $\mathbf x$는 다른 두 포인트, $x_1, x_2 \in S$의 strict convex combination으로 표현될 수 없다.

![](/imgs/mge/or3.png)

위의 예시를 다시 가져와봤다. $x_1$ 은 $\alpha x_1 + (1-\alpha)x_1 = x_1$로만 표현될 수 있고, 다른 포인트 또한 그렇다. 즉, $x_1, x_2, x_3$은 모두 EP라고 할 수 있겠다. 반면, 이 세 점을 제외한 경계나 내부는 모두 EP가 아니다.

EP가 무수히 많은 경우도 있다.

![](/imgs/mge/or4.png)

## Adjacency
우리는 두 EP에 대해, 인접한지 아닌지에 대한 여부를 직관적으로 판단할 수 있다. 가령 직사각형 모양 집합에서 대각선 방향으로 서로 바라보는 두 점은 인접하지 않을 것이다. 위의 삼각형 모양 예시에선 모든 EP가 서로 인접할 것이고.

하지만 우리는 이 인접하다는 표현을 조금 더 명확히 하고 싶다, 어떻게?

> 두 EP에 대한 라인 세그먼트가 해당 convex set의 모서리(edge)를 형성할 때, 두 EP는 **인접(adjacent)** 하다고 한다.

상상 속에서 어떤 convex set과 그것의 EP들을 생각해보자. 직관과 딱 들어맞는 정의라고 할 수 있다!

## Hyperplane
어떤 non-zero 