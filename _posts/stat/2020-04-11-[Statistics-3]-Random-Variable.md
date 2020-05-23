---
title:  "[Statistics 3] Random Variable"
tags: Statistics
toc: true
---

# Intro
지난 포스트에선 확률(probability)의 개념과 그 특성을 알아보았다. 예제를 전혀 풀지 않아서 빨리 넘어갔던 것 같다. 

이번엔 확률 변수(Random Variable, RV)에 대해 가볍게 알아보자.


# Random Variable (RV)
확률 변수(random variable)은 다음을 의미한다.

> A quantity whose value is determined by the outcome of probability experiment

풀어서 설명하자면, 확률적 시행으로 결정되는 값 정도로 볼 수 있다. 예를 들어, 주사위를 던지는 experiment에서, 주사위의 눈(1, 2, 3, 4, 5, 6)을 RV, $X$로 정의해볼 수 있다. 

RV는 "확률적 시행으로 결정된다"라는 조건만 만족하면 어떻게 정의하든 상관 없다. 주사위 던지기를 다시 생각해보자.

- 두 번 던져 나오는 눈의 합
- 한 번 던져 나오는 눈의 제곱
- 5가 나오면 0, 나머지는 1
- 무조건 0
- 한 번 던져 나오는 눈에 인접한 눈들의 합

모두 RV가 될 수 있다.

RV는 가질 수 있는 값의 성질에 따라 두 종류로 나눌 수 있다. 바로 RV가 이산적인(discrete) 경우와 연속적인(continuous) 경우다.

## Probability Notation
어떤 RV, $X$를 생각해보자. 우린 $X$가 특정한 값, $x_i$를 가질 확률에 관심이 있다. 예를 들어, 주사위의 눈을 $X$라 한다면, $X$가 1이나 3같은 특정한 값을 가질 확률을 구해야 한다. 혹은 특정한 값보다 크거나 작을 확률, 또는 그 값이 아닐 확률에 관심이 있을 수도 있다. 일반적으로 다음과 같은 노테이션을 사용한다.

> $P{X = x_i}$ : Probability that $X = x_i$

이를 변형하여 $P{X < x_i}$ 등의 부등식이나, set-builder notation을 이용하여 $P{X = x_i \vert x_i mod 5 = 3}$과 같은 표기를 할 수도 있다.


# Discrete RV
먼저, 이산적인(discrete) RV를 알아보자. Discrete RV는 이산적이기 때문에 그것의 분포(distribution)을 표로 나타낼 수 있다. 주사위 눈을 다시 생각해보자. 이는 다음과 같이 나타낼 수 있다.

$X$ | 1 | 2 | 3 | 4 | 5 | 6
---|---|---|---|---|---|---
$P(X = x_i)$ | \frac{1}{6} | \frac{1}{6} | \frac{1}{6} | \frac{1}{6} | \frac{1}{6} | \frac{1}{6}

모든 경우의 확률의 합, 즉 sample space의 확률 $P(S)$는 1임을 기억하자.

## Expectation
Discrete RV의 기댓값(expectation, expected value)은 다음과 같이 정의된다.

> $E(X) = \sum_{i=1}^n x_iP(X=x_i)$

이것은 확률에 따른 RV의 weighted average로 볼 수 있다. 

Expectation은 이산적이든 연속적이든 대부분의 성질을 공유하므로, 여기서 expectation의 일반적인 성질을 알아볼 것이다.

### Properties
가장 중요한 기댓값의 성질은 선형성(linearity)이다. 우선, 임의의 상수 $c$에 대하여 다음을 만족한다.

- $E(cX) = cE(X)$
- $E(X + c) E(X) + c$

더욱 간단하게 나타내면 다음과 같다. 임의의 상수 $a, b$에 대하여...

$E(aX + b) = aE(X) + b$ 

또, 임의의 RV, $X_1, X_2, ..., X_n$에 대해 다음이 성립한다.

$E(X_1 + ... X_n) = E(X_1) + ... + E(X_n)$



